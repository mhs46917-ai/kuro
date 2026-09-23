"""CLI: turn a folder of Gemini-generated images into a LINE sticker ZIP."""

from __future__ import annotations

import zipfile
from pathlib import Path

import click
from PIL import Image

from .constants import (
    MAIN_SIZE,
    MAX_STICKER_COUNT,
    MIN_STICKER_COUNT,
    STICKER_MAX_SIZE,
    SUPPORTED_INPUT_EXTENSIONS,
    TAB_SIZE,
)
from .processor import fit_to_canvas, find_input_images, remove_background, save_png_under_limit


@click.group()
@click.version_option()
def cli() -> None:
    """Build a LINE Creators Market sticker set from raw images."""


@cli.command()
@click.argument("input_dir", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("-o", "--output", "output_zip", type=click.Path(path_type=Path), required=True,
              help="Path to the ZIP file to write, e.g. sticker_set.zip")
@click.option("--main", "main_source", type=click.Path(exists=True, dir_okay=False, path_type=Path),
              default=None, help="Image to use for main.png (default: first sticker).")
@click.option("--tab", "tab_source", type=click.Path(exists=True, dir_okay=False, path_type=Path),
              default=None, help="Image to use for tab.png (default: first sticker).")
@click.option("--no-bg-removal", is_flag=True, default=False,
              help="Skip background removal; images are assumed already transparent.")
@click.option("--tolerance", type=int, default=30, show_default=True,
              help="Flood-fill color tolerance used by the fallback background remover.")
@click.option("--keep-dir", type=click.Path(path_type=Path), default=None,
              help="Also keep the generated PNGs in this directory (in addition to the ZIP).")
def process(
    input_dir: Path,
    output_zip: Path,
    main_source: Path | None,
    tab_source: Path | None,
    no_bg_removal: bool,
    tolerance: int,
    keep_dir: Path | None,
) -> None:
    """Convert every image in INPUT_DIR into a LINE sticker set ZIP.

    Produces main.png (240x240), tab.png (96x74), and NN.png sticker bodies
    (fit within 370x320), all transparent PNGs under LINE's 1MB limit.
    """
    images = find_input_images(input_dir, SUPPORTED_INPUT_EXTENSIONS)
    if not images:
        raise click.ClickException(f"No images found in {input_dir} (looked for {SUPPORTED_INPUT_EXTENSIONS}).")
    if len(images) > MAX_STICKER_COUNT:
        raise click.ClickException(f"Found {len(images)} images; LINE allows at most {MAX_STICKER_COUNT} stickers.")
    if len(images) < MIN_STICKER_COUNT:
        click.echo(
            f"Warning: only {len(images)} images found; LINE Creators Market requires at least "
            f"{MIN_STICKER_COUNT} stickers per set.",
            err=True,
        )

    work_dir = keep_dir or Path(output_zip).with_suffix("")
    work_dir.mkdir(parents=True, exist_ok=True)

    def load_processed(path: Path) -> Image.Image:
        img = Image.open(path)
        if not no_bg_removal:
            img = remove_background(img, tolerance=tolerance)
        return img.convert("RGBA")

    click.echo(f"Processing {len(images)} sticker(s)...")
    sticker_paths: list[Path] = []
    processed_cache: dict[Path, Image.Image] = {}
    for idx, src in enumerate(images, start=1):
        img = load_processed(src)
        processed_cache[src] = img
        sticker = fit_to_canvas(img, STICKER_MAX_SIZE)
        out_path = work_dir / f"{idx:02d}.png"
        save_png_under_limit(sticker, out_path)
        sticker_paths.append(out_path)
        click.echo(f"  {src.name} -> {out_path.name}")

    def resolve(source: Path | None) -> Image.Image:
        if source is None:
            return processed_cache[images[0]]
        if source in processed_cache:
            return processed_cache[source]
        return load_processed(source)

    main_img = resolve(main_source)
    tab_img = resolve(tab_source)

    main_path = work_dir / "main.png"
    tab_path = work_dir / "tab.png"
    save_png_under_limit(fit_to_canvas(main_img, MAIN_SIZE), main_path)
    save_png_under_limit(fit_to_canvas(tab_img, TAB_SIZE), tab_path)
    click.echo(f"  -> {main_path.name}, {tab_path.name}")

    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(main_path, arcname="main.png")
        zf.write(tab_path, arcname="tab.png")
        for p in sticker_paths:
            zf.write(p, arcname=p.name)

    if keep_dir is None:
        for p in [main_path, tab_path, *sticker_paths]:
            p.unlink()
        work_dir.rmdir()

    click.echo(f"Done: {output_zip}")


if __name__ == "__main__":
    cli()
