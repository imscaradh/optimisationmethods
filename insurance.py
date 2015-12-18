from scipy.interpolate import interp1d
from functionhelper import function as fhelper
from neldermead import neldermead
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cust_func = None
average_damage = 103
kinds = ["linear", "quadratic", "cubic"]
colors = ['r', 'b', 'g']


def main():
    rates = [50, 80, 100, 120, 150, 200, 300]
    customers = [21500, 14500, 11500, 9000, 6100, 3300, 940]
    fig = plt.figure(1, figsize=(16,9))
    ax = fig.add_subplot(111)
    fig2 = plt.figure(2)
    bx = fig2.add_subplot(111)
    for index, kind in enumerate(kinds):
        customer_by_rate = interp1d(rates,
                                    customers,
                                    kind=kind,
                                    bounds_error=False,
                                    fill_value=0.0)
        global cust_func
        cust_func = customer_by_rate
        fhelper.f = profit_for_rate
        red_patch = mpatches.Patch(color='red', label='Linear')
        blue_patch = mpatches.Patch(color='blue', label='Quadratisch')
        green_patch = mpatches.Patch(color='green', label='Kubisch')
        ax.legend(handles=[red_patch, blue_patch, green_patch], loc=4)
        bx.legend(handles=[red_patch, blue_patch, green_patch])
        ax.plot(range(103, 300), [profit_for_rate(value) for value in range(103, 300)], colors[index])
        bx.plot(range(103, 300), [customer_by_rate(value) for value in range(103, 300)], colors[index])
        best = neldermead(150, 300)
        print best
        ax.plot([best[0], best[0]], [0, best[1]], colors[index]+ ':')
        ax.plot([0, best[0]], [best[1], best[1]], colors[index]+ ':')

    plt.figure(1)
    plt.savefig("profit.png")
    plt.figure(2)
    plt.savefig("customres.png")


def profit_for_rate(rate):
    customers = cust_func(rate)
    if customers:
        income = customers * rate
        damage = average_damage * customers

        return income - damage

    else:
        return -np.inf


if __name__ == "__main__":
    main()
