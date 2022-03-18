import numpy as np
from PIL import Image
import os
import webbrowser


class Canvas:

    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color
        self.arrays = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.arrays[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.arrays, "RGB")
        os.chdir("files")
        img.save(image_path)
        webbrowser.open("file://" + os.path.realpath(image_path))
