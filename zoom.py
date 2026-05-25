import matplotlib.cm as cm
import numpy as np
from manim import *

from mandelbrot import generate_fast

# lerp = linear interpolation
# Formula: value = start + t * (end - start)
# t will be f/frames


def lerp(start, end, t):

    value = start + t * (end - start)

    return value


# start the Manim scene


class FractalScene(Scene):
    def construct(self):

        width = 800
        height = 800
        max_iter = 256
        frames = 120
        start_coord = (-2, 1, -1.5, 1.5)
        end_coord = (-0.7438, -0.7432, 0.1308, 0.1314)

        prev_image = None

        for f in range(0, frames):
            x_min = lerp(start_coord[0], end_coord[0], f / frames)
            x_max = lerp(start_coord[1], end_coord[1], f / frames)
            y_min = lerp(start_coord[2], end_coord[2], f / frames)
            y_max = lerp(start_coord[3], end_coord[3], f / frames)

            view = generate_fast(width, height, max_iter, x_min, x_max, y_min, y_max)

            colored = (cm.inferno(view / max_iter) * 255).astype(np.uint8)

            if prev_image is not None:
                self.remove(prev_image)

            image = ImageMobject(colored)
            image.set_height(config.frame_height)
            self.add(image)
            image.move_to(ORIGIN)
            self.wait(1 / 30)

            prev_image = image

        self.play(FadeOut(image), run_time=2)
