import matplotlib.cm as cm
import numpy as np
from manim import *

from mandelbrot import generate, mandelbrot

# lerp = linear interpolation
# Formula: value = start + t * (end - start)
# t will be f/frames


def lerp(start, end, t):

    value = start + t * (end - start)

    return value


# start the Manim scene:


class FractalScene(Scene):
    def construct(self):

        width = 200
        height = 200
        max_iter = 256
        frames = 10
        start_coord = (-2, 1, -1.5, 1.5)
        end_coord = (-0.7485, -0.7385, 0.1264, 0.1364)

        prev_image = None

        for f in range(0, 100):
            x_min = lerp(start_coord[0], end_coord[0], f / frames)
            x_max = lerp(start_coord[1], end_coord[1], f / frames)
            y_min = lerp(start_coord[2], end_coord[2], f / frames)
            y_max = lerp(start_coord[3], end_coord[3], f / frames)

            view = generate(width, height, max_iter, x_min, x_max, y_min, y_max)

            colored = (cm.inferno(view / max_iter) * 255).astype(np.uint8)

            if prev_image is not None:
                self.remove(prev_image)

            image = ImageMobject(colored)
            image.scale_to_fit_height(config.frame_height)
            self.add(image)
            self.wait(1 / 30)

            prev_image = image
