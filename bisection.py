import numpy as np
import functionhelper.function as fhelper
import matplotlib.pyplot as plt

global ax


def main():
    fhelper.func = raw_input("Enter a function: ")
    a = int(input("Enter x-LEFT: "))
    b = int(input("Enter x-RIGHT: "))

    x_range = np.arange(-50, 50)
    fig = plt.figure()
    global ax
    ax = fig.add_subplot(111)
    ax.plot(x_range, [fhelper.f(value) for value in x_range])

    ax.plot((a, a), (0, fhelper.f(a) + 30), 'r-')
    ax.plot((b, b), (0, fhelper.f(b) + 30), 'r-')

    result = bisect(a, b)
    print(result)

    plt.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.savefig("doc/bisektion.png")


def bisect(a, b):
    c = (a + b) / 2
    ax.plot((c, c), (0, fhelper.f(c) + 30), 'r-')
    if abs(fhelper.df(c)) < 0.001:
        return c
    elif fhelper.df(c) < 0:
        return bisect(c, b)
    else:
        return bisect(a, c)


if __name__ == '__main__':
    main()
