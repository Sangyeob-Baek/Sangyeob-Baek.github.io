import sys
from PIL import Image, ImageFilter
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
cx, bottom, side = 520, 955, 880          # person centre x (head and body both ~520), cut above the jeans
box = (cx - side // 2, bottom - side, cx + side // 2, bottom)
im = im.crop(box).resize((2048, 2048), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
im.save(out, quality=92, optimize=True); print(box, im.size)
