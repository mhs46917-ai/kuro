"""Core image processing: background removal, resizing, and size-limit enforcement."""

from __future__ import annotations

import io
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .constants import DEFAULT_FONT_CANDIDATES, MAX_FILE_SIZE_BYTES

try:
    from rembg import remove as _rembg_remove
except ImportError:  # rembg (ML background removal) is an optional extra.
    _rembg_remove = None


def remove_background(image: Image.Image, tolerance: int = 30) -> Image.Image:
    """Strip the background, preferring rembg (ML) and falling back to a
    corner flood-fill for images shot on a plain/solid background."""
    if _rembg_remove is not None:
        return _rembg_remove(image.convert("RGBA"))
    return _flood_fill_background(image, tolerance)


def _flood_fill_background(image: Image.Image, tolerance: int) -> Image.Image:
    img = image.convert("RGBA")
    w, h = img.size
    seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (0, h // 2)]
    for seed in seeds:
        try:
            ImageDraw.floodfill(img, seed, (0, 0, 0, 0), thresh=tolerance)
        except (IndexError, ValueError):
            continue
    return img


def fit_to_canvas(image: Image.Image, canvas_size: tuple[int, int]) -> Image.Image:
    """Scale `image` (preserving aspect ratio, upscaling if needed) so its
    largest dimension matches the canvas, then center it on a transparent
    canvas of exactly `canvas_size`."""
    target_w, target_h = canvas_size
    img = image.convert("RGBA")
    src_w, src_h = img.size
    scale = min(target_w / src_w, target_h / src_h)
    new_w, new_h = max(1, round(src_w * scale)), max(1, round(src_h * scale))
    resized = img.resize((new_w, new_h), Image.LANCZOS)

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


def add_text_caption(
    image: Image.Image,
    text: str,
    *,
    font_path: str,
    font_size: int = 48,
    fill: str = "black",
    stroke_fill: str = "white",
    stroke_width: int = 6,
    margin: tuple[int, int] = (16, 12),
) -> Image.Image:
    """Draw `text` at the top-left corner of `image`, with a colored fill and
    a thick outline stroke so it stays readable over any sticker artwork."""
    img = image.convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(margin, text, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)
    return img
