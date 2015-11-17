import numpy as np
import matplotlib.pyplot as plt
from decimal import *

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.axis([-5, 5, -10, 10])
    plt.savefig("testplot1.pdf")
