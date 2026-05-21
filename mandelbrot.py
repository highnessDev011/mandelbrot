from math import log

import matplotlib.pyplot as plt
import numpy as np

# function takes a complex number c and a max iteration count
# Return: num of iterations it took to escape or max_iter if it never did


def mandelbrot(c, max_iter):

    # start at 0
    z = 0

    for i in range(max_iter):
        z = z**2 + c

        if abs(z) > 2:
            return i - log(log(abs(z))) / log(2)

    return max_iter


def generate(width, height, max_iter, x_min=-2, x_max=1, y_min=-1.5, y_max=1.5):

    result = np.zeros((height, width))

    for row in range(height):
        for col in range(width):
            x = x_min + col / (width - 1) * (x_max - x_min)
            y = y_min + row / (height - 1) * (y_max - y_min)
            c = complex(x, y)

            result[row][col] = mandelbrot(c, max_iter)

    return result


def renderer(width, height, max_iter, x_min, x_max, y_min, y_max):

    view = generate(width, height, max_iter, x_min, x_max, y_min, y_max)
    plt.imshow(view, cmap="inferno")

    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    renderer(800, 800, 256, -1.77, -1.73, -0.02, 0.02)
