import functionhelper.function as fhelper
import matplotlib.pyplot as plt

global ax


def main():
    fhelper.func = raw_input("Enter function: ")
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))

    result = neldermead(x1, x2)
    print(result)


def neldermead(x1, x2):
    if fhelper.f(x1) > fhelper.f(x2):
        x1, x2 = x2, x1

    xc = 0.5 * (x1 + x2)
    xr = x1 + (x1 - x2)
    xe = x1 + 2 * (x1 - x2)

    if abs(fhelper.df(x2)) < 0.001:
        return x2

    if fhelper.f(xr) >= fhelper.f(x1):
        return neldermead(x1, xc)
    elif fhelper.f(xe) < fhelper.f(xr) < fhelper.f(x1):
        return neldermead(x1, xe)
    elif fhelper.f(xe) >= fhelper.f(xr) < fhelper.f(x1):
        return neldermead(x1, xr)


if __name__ == '__main__':
    main()
