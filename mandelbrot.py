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
            return i

    return max_iter


def generate(width, height, max_iter):

    result = np.zeros((height, width))

    for row in range(height):
        for col in range(width):
            x = -2 + col / (width - 1) * 3
            y = -1.5 + row / (height - 1) * 3
            c = complex(x, y)

            result[row][col] = mandelbrot(c, max_iter)

    return result


def renderer(width, height, max_iter):

    view = generate(width, height, max_iter)
    plt.imshow(view, cmap="inferno")

    plt.show()
    plt.axis("off")


if __name__ == "__main__":
    renderer(800, 800, 100)
