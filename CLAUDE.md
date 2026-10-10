# Sticker set defaults

Unless the user says otherwise, build every LINE sticker set at the agreed size and with outlined captions:

```
python -m line_sticker.cli process <cells_dir> -o <zip> --margin 0.085 --text-outline 4.5 --main <cell> --tab <cell>
```

- `--margin 0.085`: each sticker's content (caption + character) is fit inside the 370x320 canvas leaving 8.5% of each dimension empty on every side (about 27px top/bottom, content ~266px tall). The user settled on this after 0.23 and 0.175 both looked too small. Size from this margin, not from a fixed scale, so sets from different source resolutions look the same.
- `--text-outline 4.5`: white outline, 4.5px at sticker size, around the caption text drawn into the artwork.
- Add `--trim 3` for single full-frame images (not grid cells), which often have a dark 1-2px compression rim.
- Grid images: split into cells first at the real background gutters per row (and inside white grid lines when present), skipping the cells the user asks to drop.
