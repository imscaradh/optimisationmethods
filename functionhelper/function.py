from scipy.misc.common import derivative
import math

global func


def f(x):
    return eval(func)


def tan(x_range, x):
    return f(x) + df(x) * (x_range - x)


def df(x):
    return derivative(f, x, dx=1e-6)
