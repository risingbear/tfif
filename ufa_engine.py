# ufa_engine.py — Basic Mandelbrot Fractal Renderer (CPU)
import numpy as np
from PIL import Image

def generate_fractal(width=800, height=800, max_iter=256, zoom=1.0, center=(0, 0)):
    x_center, y_center = center
    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + x_center
            zy = (y - height / 2) / (0.5 * zoom * height) + y_center
            z = zx + zy * 1j
            c = z
            iter = 0
            while abs(z) < 4 and iter < max_iter:
                z = z * z + c
                iter += 1
            color = 255 - int(iter * 255 / max_iter)
            pixels[x, y] = (color, color, color)

    image.save("ufa_output.png")
    return "ufa_output.png"
