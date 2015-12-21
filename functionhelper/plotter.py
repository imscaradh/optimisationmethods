import numpy as np
import matplotlib.pyplot as plt
from decimal import *
import matplotlib.patches as mpatches


def graph(formula, x_range, yaxis, name, lines=[]):
    x = np.array(x_range)
    #y = eval(formula)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, [formula(value) for value in x])
    #plt.axis([-10000, 400000, 103, 300])
    plt.grid(True)
    ax.set_xlabel("Rate")
    ax.set_ylabel(yaxis)
    for line in lines:
        ax.axvline(x=line[0], ymax=line[1], color="r")
    plt.savefig("%s.png" % (name))
