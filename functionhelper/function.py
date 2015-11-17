from scipy.misc.common import derivative

global func


def f(x):
    return eval(func)


def df(x):
    return derivative(f, x, dx=1e-6)
