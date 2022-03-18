import numpy as np
from PIL import Image

# create 3d pixels with zeros, and change green pixels.

pixels = np.zeros((5, 4, 3), dtype="uint8")
pixels[:] = [255, 255, 0]
pixels[1:4] = [0, 255, 0]
img = Image.fromarray(pixels, "RGB")
img.save("canvas.png")
