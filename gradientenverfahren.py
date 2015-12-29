import numpy as np
import functionhelper.function as fhelper
import matplotlib.pyplot as plt


def main():
    fhelper.func = raw_input("Enter function: ")

    x_range = np.arange(-50, 50)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_range, [fhelper.f(value) for value in x_range])

    lmbda = 0.001
    point = -5
    df_result = fhelper.df(point)
    while abs(df_result) > lmbda * 0.1:
        df_result = fhelper.df(point)
        point -= lmbda * df_result

    print(point)

    point1 = -40
    x_range_tan = np.arange(point1 - 20, point1 + 20)
    ax.plot(x_range_tan, fhelper.tan(x_range_tan, point1))

    point2 = -20
    x_range_tan = np.arange(point2 - 20, point2 + 20)
    ax.plot(x_range_tan, fhelper.tan(x_range_tan, point2))

    x_range_tan = np.arange(point - 20, point + 20)
    ax.plot(x_range_tan, fhelper.tan(x_range_tan, point))

    plt.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.savefig("doc/gradient.png")


if __name__ == '__main__':
    main()
