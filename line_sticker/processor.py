"""Core image processing: background removal, resizing, and size-limit enforcement."""

from __future__ import annotations

import io
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

from .constants import DEFAULT_FONT_CANDIDATES, MAX_FILE_SIZE_BYTES

try:
    from rembg import remove as _rembg_remove
except ImportError:  # rembg (ML background removal) is an optional extra.
    _rembg_remove = None


def remove_background(image: Image.Image, tolerance: int = 30) -> Image.Image:
    """Strip the background, preferring rembg (ML) and falling back to a
    color-key removal for images shot on a plain/solid background."""
    if _rembg_remove is not None:
        return _rembg_remove(image.convert("RGBA"))
    return _color_key_background(image, tolerance)


def _color_distance(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(c1, c2))


def _dominant_border_color(img: Image.Image) -> tuple[int, int, int]:
    """Sample colors all along the image's border, cluster them (by a fixed
    small tolerance), and return only the single largest cluster's average
    color as the background reference. Using just the biggest cluster -
    rather than every cluster above some share of the perimeter - matters
    because subject content can legitimately touch a large stretch of the
    crop's edge (a prop, a limb, a pale fur patch), and such content must
    never be mistaken for a second background color just because it covers
    a sizeable fraction of the border; the true background is reliably the
    majority color since the subject is roughly centered in each cell."""
    w, h = img.size
    step = max(1, min(w, h) // 200)
    xs = range(0, w, step)
    ys = range(0, h, step)
    samples = (
        [img.getpixel((x, 0))[:3] for x in xs]
        + [img.getpixel((x, h - 1))[:3] for x in xs]
        + [img.getpixel((0, y))[:3] for y in ys]
        + [img.getpixel((w - 1, y))[:3] for y in ys]
    )

    clusters: list[list[tuple[int, int, int]]] = []
    for color in samples:
        for cluster in clusters:
            if _color_distance(color, cluster[0]) <= 30:
                cluster.append(color)
                break
        else:
            clusters.append([color])

    clusters.sort(key=len, reverse=True)
    best = clusters[0]
    return tuple(sum(c[i] for c in best) // len(best) for i in range(3))


_FRINGE_GAP_CLOSE = 3
# 800px on a ~337px grid cell, the size `max_enclosed_size` was tuned on.
_ENCLOSED_AREA_FRACTION = 0.007
_MIN_FRINGE_TOLERANCE = 90


def _color_key_background(
    image: Image.Image,
    tolerance: int,
    max_enclosed_size: int | None = None,
    fringe_width: int = 20,
    fringe_tolerance: int = 180,
) -> Image.Image:
    """Make background-colored pixels transparent, but only the ones
    actually connected to the image's border through other background-
    colored pixels - not every pixel that merely happens to be close to the
    background color wherever it occurs.

    That connectivity requirement is what keeps this safe at a tolerance
    loose enough to clear real-world noise (JPEG grain, unеven lighting on a
    photographed background): a subject can legitimately contain small
    patches close to the background color - a pastel prop, a blanket dyed to
    match, pencil-shading texture that fades toward paper-white inside an
    eye patch - and those never connect through to the border because they
    sit inside a region the subject's own (very different-colored) outline
    or fill surrounds. Only a contiguous blob that actually reaches the
    frame's edge is background. The tradeoff is that this no longer reaches
    background trapped in pockets fully enclosed by the subject (between
    paws, between letters of outlined text) the way the old flood fill
    couldn't either - but wrongly eating real content is the worse failure,
    and there's no reliable way to tell "a real enclosed gap" apart from "a
    subject detail that happens to be background-colored" by color alone.

    Small enclosed pockets (not reachable from the border) are removed too,
    up to `max_enclosed_size` pixels - a gap between two letters' strokes or
    between a loop's ends is typically a few hundred pixels at most, while a
    subject detail that happens to share the background color (a matching
    blanket, a pastel prop) is a much larger blob. There's still no way to
    tell the two apart by color alone, so size is the only signal available,
    and a large enclosed blob is left alone rather than risk erasing real
    content. The limit scales with the image's area (default: 0.7%, never
    under 800px), since the same letter's counter is ten times as many pixels
    in a 900x1200 frame as in a grid cell a third the width.

    Finally, the cut edge is swept outward up to `fringe_width` pixels, to
    catch the anti-aliased blend band around an outline that a tight
    `tolerance` alone leaves behind as a visible color-tinted edge (hand-drawn
    pencil art can fade from pure background to the outline's dark ink over
    15-20px). Three things keep this from eating real content:

    - It only grows through pixels within `fringe_tolerance` of the
      background, one step at a time from the already-cleared area, so a dark
      outline stops it instead of letting it jump across to the fill behind.
      Hand-drawn outlines have small breaks, so the barrier is first closed
      over gaps of a few pixels; otherwise it leaks through a break and eats
      a diamond-shaped hole in the fill.
    - `fringe_tolerance` is capped at half the color distance from the
      background to pure white. A pale background (mint, cream) sits close to
      white fur or a pastel prop, so the same absolute tolerance that is safe
      on a vivid blue background would reach right into them; scaling to the
      background keeps the sweep short of the lightest content in any case.
    - On a pale background the sweep is skipped altogether (when the capped
      tolerance is under `_MIN_FRINGE_TOLERANCE`). Content there - an
      off-white bag, a grey mat - sits only a few units past `tolerance`
      from the background, so no sweep tolerance can both reach a blend band
      and spare it, while a pale background's blend band is barely visible
      anyway.
    - It is kept well under the distance a flat pale fill (a bowl's grey, a
      pillow's cream) sits at, accepting a barely visible hairline left on
      the darkest part of a wide blend over erasing real fill, the safer
      failure."""
    img = image.convert("RGBA")
    ref = _dominant_border_color(img)

    arr = np.asarray(img).astype(np.float32)
    rgb, alpha = arr[..., :3], arr[..., 3]
    ref_arr = np.array(ref, dtype=np.float32)

    dist = np.abs(rgb - ref_arr).sum(axis=2)
    candidate = dist <= tolerance

    if max_enclosed_size is None:
        max_enclosed_size = max(800, round(candidate.size * _ENCLOSED_AREA_FRACTION))

    labeled, n_components = ndimage.label(candidate, structure=np.ones((3, 3), dtype=int))
    border_labels = set(
        np.unique(labeled[0, :])
    ) | set(np.unique(labeled[-1, :])) | set(np.unique(labeled[:, 0])) | set(np.unique(labeled[:, -1]))
    border_labels.discard(0)

    sizes = ndimage.sum(candidate, labeled, index=np.arange(1, n_components + 1)) if n_components else np.array([])
    removable_labels = set(border_labels)
    removable_labels.update(i + 1 for i, size in enumerate(sizes) if size <= max_enclosed_size)
    is_background = np.isin(labeled, list(removable_labels)) if removable_labels else np.zeros_like(candidate)

    fringe_limit = min(fringe_tolerance, float(np.abs(255.0 - ref_arr).sum()) / 2)
    if fringe_limit >= _MIN_FRINGE_TOLERANCE and fringe_width > 0:
        loose = dist <= fringe_limit
        barrier = ~loose & ~is_background
        pad = _FRINGE_GAP_CLOSE + 1
        barrier = ndimage.binary_closing(
            np.pad(barrier, pad, mode="edge"),
            structure=np.ones((3, 3), dtype=bool),
            iterations=_FRINGE_GAP_CLOSE,
        )[pad:-pad, pad:-pad]
        is_background = ndimage.binary_dilation(
            is_background,
            structure=ndimage.generate_binary_structure(2, 1),
            iterations=fringe_width,
            mask=(loose & ~barrier) | is_background,
        )

    new_alpha = np.where(is_background, 0.0, alpha)
    out = np.dstack([rgb, new_alpha]).astype(np.uint8)
    return Image.fromarray(out, mode="RGBA")


def clear_edge_specks(image: Image.Image, max_size: int = 400) -> Image.Image:
    """Clear small opaque pieces (at most `max_size` pixels) touching the image
    edge. After background removal these are leftover background - a corner of
    vignette, a compression rim - since real content is rarely a sliver cut by
    the frame. Larger edge-touching pieces (a blanket running off the frame)
    are kept."""
    img = image.convert("RGBA")
    alpha = np.asarray(img.getchannel("A")) > 0
    labeled, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=int))
    if count == 0:
        return img
    edge = set(np.unique(labeled[0])) | set(np.unique(labeled[-1])) | set(np.unique(labeled[:, 0])) | set(np.unique(labeled[:, -1]))
    edge.discard(0)
    sizes = ndimage.sum(alpha, labeled, index=np.arange(1, count + 1))
    specks = [label for label in edge if sizes[label - 1] <= max_size]
    if not specks:
        return img
    arr = np.asarray(img).copy()
    arr[..., 3] = np.where(np.isin(labeled, specks), 0, arr[..., 3])
    return Image.fromarray(arr, mode="RGBA")


def crop_to_content(image: Image.Image, margin: int = 4) -> Image.Image:
    """Crop a background-removed image to its visible content plus `margin`,
    after clearing edge specks so a leftover corner can't stretch the crop box
    back out to the whole frame."""
    img = clear_edge_specks(image)
    alpha = np.asarray(img.getchannel("A")) > 0
    ys, xs = np.where(alpha)
    if len(ys) == 0:
        return img
    h, w = alpha.shape
    return img.crop((
        max(0, xs.min() - margin),
        max(0, ys.min() - margin),
        min(w, xs.max() + 1 + margin),
        min(h, ys.max() + 1 + margin),
    ))


def clear_specks(image: Image.Image, max_size: int = 12) -> Image.Image:
    """Clear isolated opaque specks of at most `max_size` pixels anywhere (1-3px
    JPEG noise that survives background removal), so they neither show up nor
    stretch the content bounding box."""
    img = image.convert("RGBA")
    alpha = np.asarray(img.getchannel("A")) > 0
    labeled, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=int))
    if count == 0:
        return img
    sizes = ndimage.sum(alpha, labeled, index=np.arange(1, count + 1))
    specks = [i + 1 for i, size in enumerate(sizes) if size <= max_size]
    if not specks:
        return img
    arr = np.asarray(img).copy()
    arr[..., 3] = np.where(np.isin(labeled, specks), 0, arr[..., 3])
    return Image.fromarray(arr, mode="RGBA")


def margin_box(canvas_size: tuple[int, int], margin: float) -> tuple[float, float]:
    """Inner box left after reserving `margin` (a fraction of each dimension) on every side."""
    w, h = canvas_size
    return w * (1 - 2 * margin), h * (1 - 2 * margin)


def fit_with_margin(image: Image.Image, canvas_size: tuple[int, int], margin: float) -> Image.Image:
    """Crop to visible content, then scale it to fit inside the canvas leaving
    `margin` of each dimension empty on every side, centered. Sizing from the
    margin instead of a fixed scale gives every sticker the same amount of
    breathing room whatever the source image's resolution or framing."""
    img = image.convert("RGBA")
    bbox = img.getbbox()
    if bbox is None:
        return Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    img = img.crop(bbox)
    box_w, box_h = margin_box(canvas_size, margin)
    scale = min(box_w / img.width, box_h / img.height)
    new_w, new_h = max(1, round(img.width * scale)), max(1, round(img.height * scale))
    resized = _resize_premultiplied(img, (new_w, new_h))
    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    canvas.paste(resized, ((canvas_size[0] - new_w) // 2, (canvas_size[1] - new_h) // 2), resized)
    return canvas


def outline_caption(image: Image.Image, radius: float) -> Image.Image:
    """Put a white outline of `radius` px around caption text drawn into the
    artwork (dark lettering above the character).

    The caption is the line of dark "ink" near the top: dark pixels are
    smeared sideways so glyphs merge into blobs, the biggest short blob in
    the top third is the caption, and other short blobs on the same rows (a
    long dash's far side, a dakuten, a detached stroke) are pulled in.
    Pieces clearly lighter than the lettering (an outlined confetti scrap)
    are dropped. The outline is painted over decorations
    behind the text (rays, sparkles) but under the text itself, and the
    text's own background-tinted anti-aliased edge is lightened into white
    so no ring of the old background shows between text and outline."""
    img = image.convert("RGBA")
    pad = int(np.ceil(radius)) + 2
    padded = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    padded.paste(img, (pad, pad))
    arr = np.asarray(padded).astype(np.float32)
    rgb, a = arr[..., :3], arr[..., 3] / 255
    opaque = a > 0
    lum = rgb @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    ink = opaque & (lum < 140)
    labeled, count = ndimage.label(ink, structure=np.ones((3, 3), dtype=int))
    if count:
        sizes = ndimage.sum(ink, labeled, index=np.arange(1, count + 1))
        ink = np.isin(labeled, [i + 1 for i, size in enumerate(sizes) if size >= 10])
    rows = np.where(ink.any(axis=1))[0]
    if len(rows) == 0:
        return img
    smear = ndimage.binary_dilation(ink, structure=np.ones((3, 25), dtype=bool))
    blobs, blob_count = ndimage.label(smear, structure=np.ones((3, 3), dtype=int))
    spans = ndimage.find_objects(blobs)
    height = ink.shape[0]
    ink_counts = ndimage.sum(ink, blobs, index=np.arange(1, blob_count + 1))
    # a caption line is short and near the top; the character is far taller
    short = [i for i, sl in enumerate(spans) if sl[0].stop - sl[0].start < 0.35 * height]
    candidates = [i for i in short if spans[i][0].start < 0.35 * height]
    if not candidates:
        return img
    main = max(candidates, key=lambda i: ink_counts[i])
    top, bottom = spans[main][0].start, spans[main][0].stop
    selected = {main}
    changed = True
    while changed:  # pull in the rest of the line: a long dash, a dakuten, a detached stroke
        changed = False
        for i in short:
            if i not in selected and spans[i][0].start <= bottom + 4 and spans[i][0].stop >= top - 4:
                selected.add(i)
                top, bottom = min(top, spans[i][0].start), max(bottom, spans[i][0].stop)
                changed = True
    caption_ink = ink & np.isin(blobs, [i + 1 for i in selected])
    # drop pieces clearly lighter than the lettering (outlined confetti caught on the line)
    pieces, piece_count = ndimage.label(caption_ink, structure=np.ones((3, 3), dtype=int))
    if piece_count:
        mean_lum = ndimage.mean(lum, pieces, index=np.arange(1, piece_count + 1))
        weight = ndimage.sum(caption_ink, pieces, index=np.arange(1, piece_count + 1))
        order = np.argsort(mean_lum)
        base = mean_lum[order][np.searchsorted(np.cumsum(weight[order]), weight.sum() / 2)]
        caption_ink = np.isin(pieces, [i + 1 for i in range(piece_count) if mean_lum[i] <= base + 25])
    text = ndimage.binary_dilation(caption_ink, iterations=2) & opaque

    lighten = np.clip((230 - lum) / 160, 0, 1)[..., None]
    text_rgb = rgb * lighten + 255 * (1 - lighten)
    stroke = np.clip(radius + 0.5 - ndimage.distance_transform_edt(~text), 0, 1)

    out_rgb = rgb * (1 - stroke[..., None]) * a[..., None] + 255 * stroke[..., None]
    out_a = a * (1 - stroke) + stroke
    t = text & (a > 0)
    ta = np.where(t, a, 0)
    out_rgb = text_rgb * ta[..., None] + out_rgb * (1 - ta[..., None])
    out_a = ta + out_a * (1 - ta)
    out_rgb = out_rgb / np.maximum(out_a, 1e-6)[..., None]
    out = np.dstack([out_rgb, out_a * 255]).clip(0, 255).astype(np.uint8)
    return Image.fromarray(out, mode="RGBA").crop(Image.fromarray(out, mode="RGBA").getbbox())


def _resize_premultiplied(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize an RGBA image the way `Image.resize` does not: with RGB
    premultiplied by alpha beforehand (and divided back out after). Plain
    per-channel resampling blends each channel independently, so a fully
    transparent pixel's leftover background color still gets mixed into a
    neighboring semi-transparent edge pixel's RGB during the resize's
    interpolation - visible as a thin ring tinted with the background color
    around every outline once the sticker is scaled up onto its canvas.
    Premultiplying first means a transparent pixel contributes zero color to
    that blend, matching how compositing actually works."""
    arr = np.asarray(img.convert("RGBA")).astype(np.float32)
    rgb, alpha = arr[..., :3], arr[..., 3:4]
    premultiplied = (rgb * (alpha / 255.0)).astype(np.uint8)

    premultiplied_resized = np.asarray(
        Image.fromarray(premultiplied, mode="RGB").resize(size, Image.LANCZOS)
    ).astype(np.float32)
    alpha_resized = np.asarray(
        Image.fromarray(alpha[..., 0].astype(np.uint8), mode="L").resize(size, Image.LANCZOS)
    ).astype(np.float32)

    safe_alpha = np.clip(alpha_resized, 1, 255)[..., None]
    rgb_resized = np.clip(premultiplied_resized * 255.0 / safe_alpha, 0, 255)

    out = np.dstack([rgb_resized, alpha_resized]).astype(np.uint8)
    return Image.fromarray(out, mode="RGBA")


def fit_to_canvas(image: Image.Image, canvas_size: tuple[int, int]) -> Image.Image:
    """Scale `image` (preserving aspect ratio, upscaling if needed) so its
    largest dimension matches the canvas, then center it on a transparent
    canvas of exactly `canvas_size`."""
    target_w, target_h = canvas_size
    img = image.convert("RGBA")
    src_w, src_h = img.size
    scale = min(target_w / src_w, target_h / src_h)
    new_w, new_h = max(1, round(src_w * scale)), max(1, round(src_h * scale))
    resized = _resize_premultiplied(img, (new_w, new_h))

    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    offset = ((target_w - new_w) // 2, (target_h - new_h) // 2)
    canvas.paste(resized, offset, resized)
    return canvas


def save_png_under_limit(image: Image.Image, path: Path, max_bytes: int = MAX_FILE_SIZE_BYTES) -> None:
    """Save as PNG, optimizing (and if needed, quantizing) to stay under
    LINE's per-file size limit."""
    path.parent.mkdir(parents=True, exist_ok=True)

    buf = io.BytesIO()
    image.save(buf, format="PNG", optimize=True)
    if buf.tell() <= max_bytes:
        path.write_bytes(buf.getvalue())
        return

    # Still too large: quantize to a palette while preserving alpha.
    alpha = image.getchannel("A")
    quantized = image.convert("RGB").convert(
        "P", palette=Image.ADAPTIVE, colors=256
    )
    quantized.putalpha(alpha)
    buf = io.BytesIO()
    quantized.save(buf, format="PNG", optimize=True)
    path.write_bytes(buf.getvalue())


def find_input_images(input_dir: Path, extensions: tuple[str, ...]) -> list[Path]:
    files = [p for p in input_dir.iterdir() if p.suffix.lower() in extensions and p.is_file()]
    return sorted(files, key=lambda p: p.name)


def resolve_font_path(font_path: str | Path | None) -> str:
    """Return a usable font file path, defaulting to a bundled Japanese-capable
    font if none is given."""
    if font_path:
        if not Path(font_path).is_file():
            raise FileNotFoundError(f"Font file not found: {font_path}")
        return str(font_path)
    for candidate in DEFAULT_FONT_CANDIDATES:
        if Path(candidate).is_file():
            return candidate
    raise FileNotFoundError(
        "No default font found; pass --font pointing to a .ttf/.otf file."
    )


def fit_to_canvas_with_caption(
    image: Image.Image,
    canvas_size: tuple[int, int],
    text: str,
    *,
    font_path: str,
    font_size: int = 48,
    fill: str = "black",
    stroke_fill: str = "white",
    stroke_width: int = 6,
    top_margin: int = 8,
    text_gap: int = 4,
    side_margin: int = 6,
    image_scale: float = 1.0,
) -> Image.Image:
    """Reserve a horizontally-centered text band at the top of the canvas,
    then scale `image` (preserving aspect ratio) to fit the remaining space
    below it, so the artwork never overlaps the caption."""
    target_w, target_h = canvas_size
    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(font_path, font_size)

    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = (target_w - text_w) / 2 - bbox[0]
    text_y = top_margin - bbox[1]
    draw.text((text_x, text_y), text, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)

    reserved_h = top_margin + text_h + text_gap
    avail_w = max(1, target_w - 2 * side_margin)
    avail_h = max(1, target_h - reserved_h - side_margin)

    img = image.convert("RGBA")
    src_w, src_h = img.size
    scale = min(avail_w / src_w, avail_h / src_h) * image_scale
    # Never let the artwork spill past the canvas edges (that would get
    # silently clipped on paste): cap the scale to what actually fits below
    # the caption, full width included.
    max_scale = min(target_w / src_w, max(1, target_h - reserved_h) / src_h)
    scale = min(scale, max_scale)
    new_w, new_h = max(1, round(src_w * scale)), max(1, round(src_h * scale))
    resized = _resize_premultiplied(img, (new_w, new_h))

    # Anchor the artwork right under the caption (instead of centering it in
    # the leftover space) so text and image sit close together, with any
    # slack left as bottom margin rather than splitting it above the image.
    offset_x = (target_w - new_w) // 2
    offset_y = round(reserved_h)
    canvas.paste(resized, (offset_x, offset_y), resized)
    return canvas
