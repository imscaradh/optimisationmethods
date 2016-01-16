import numpy as np
import functionhelper.function as fhelper
import matplotlib.pyplot as plt
import time


def algorithm(point, lmbda):
    fhelper.func = "x**2"  # raw_input("Enter function: ")

    x_range = np.arange(-50, 50)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt_func, = ax.plot(x_range, [fhelper.f(value) for value in x_range], label=fhelper.func)
    plt.legend(handles=[plt_func])

    # Algorithm
    df_result = fhelper.df(point)
    while abs(df_result) > abs(lmbda * 0.1):
        df_result = fhelper.df(point)
        point -= lmbda * df_result

    print("Extremalstelle bei x = %f" % point)

    # Plot approximation
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


def main():
    algorithm(-5, 0.01)
    
    # values = np.arange(0.0001, 2, 0.05)
    # for lmdba in values:
    # print("Run with lambda = %s --------------------------------" % lmdba)
    # t1 = time.time()
    # algorithm(lmdba)
    # t2 = time.time()
    # delta = t2 - t1
    # print("Took %f ms \n" % delta)


if __name__ == '__main__':
    main()
