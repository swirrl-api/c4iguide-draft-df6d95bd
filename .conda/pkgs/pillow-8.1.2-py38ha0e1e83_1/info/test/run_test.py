#  tests for pillow-8.1.2-py38ha0e1e83_1 (this is a generated file);
print('===== testing package: pillow-8.1.2-py38ha0e1e83_1 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import fsspec

from PIL import Image


# Test JPEG2k
with fsspec.open("https://www.fnordware.com/j2k/relax.jp2") as f:
  image = Image.open(f)
  image.load()

#  --- run_test.py (end) ---

print('===== pillow-8.1.2-py38ha0e1e83_1 OK =====');
print("import: 'PIL'")
import PIL

print("import: 'PIL.Image'")
import PIL.Image

print("import: 'PIL.ImageCms'")
import PIL.ImageCms

