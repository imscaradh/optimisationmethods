import numpy as np
import functionhelper.function as fhelper
import matplotlib.pyplot as plt

global ax


def main():
    fhelper.func = "math.sqrt(100**2+(2*100-x)**2)/2.1+math.sqrt(100**2+x**2)/4.1"

    x_range = np.arange(-150, 400)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_range, [fhelper.f(value) for value in x_range])

    plt.grid(True)
    ax.set_xlabel("Way [x]")
    ax.set_ylabel("Time [t]")
    plt.savefig("doc/lifeguard_100.png")


if __name__ == '__main__':
    main()
