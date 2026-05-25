from math import log

import matplotlib
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


# This function is vectorized - x, y are 1D arrays — np.meshgrid transforms them into 2D grids
# C is used to compute the complex numbers
# Z is used to create a 2d array of zeroes
# Generates all pixels, coordinates and checks which 'escaped'


def generate_fast(width, height, max_iter, x_min=-2, x_max=1, y_min=-1.5, y_max=1.5):

    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    X, Y = np.meshgrid(x, y)

    C = X + 1j * Y

    Z = np.zeros_like(C)

    iterations = np.zeros_like(C, dtype=float)

    mask = np.ones(C.shape, dtype=bool)

    # iterate max_iter times, only updating points that haven't escaped
    for i in range(max_iter):
        Z[mask] = Z[mask] ** 2 + C[mask]
        escaped = abs(Z) > 2  # check which points have gone past the escape boundary

        iterations[escaped & mask] = i

        mask[escaped] = False

    return iterations


def renderer(width, height, max_iter, x_min, x_max, y_min, y_max):

    view = generate_fast(width, height, max_iter, x_min, x_max, y_min, y_max)
    plt.imshow(view, cmap="inferno")

    plt.axis("off")
    plt.savefig("preview.png", bbox_inches="tight", dpi=150)
    plt.show()


# renderer here for when you run with py mandelbrot.py will show a preview image
if __name__ == "__main__":
    renderer(800, 800, 256, -2, 1, -1.5, 1.5)
