"""LINE Creators Market sticker size/format requirements."""

# Sticker body: fits within this box, transparent PNG.
STICKER_MAX_SIZE = (370, 320)

# Main image: shown as the set's icon.
MAIN_SIZE = (240, 240)

# List/tab image: shown in the sticker tray.
TAB_SIZE = (96, 74)

MIN_STICKER_COUNT = 8
MAX_STICKER_COUNT = 40

MAX_FILE_SIZE_BYTES = 1024 * 1024  # 1 MB per image

SUPPORTED_INPUT_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".bmp")
