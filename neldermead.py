import functionhelper.function as fhelper


def main():
    fhelper.func = (input("Enter function: "))
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))

    result = neldermead(x1, x2)
    print(result)


def neldermead(x1, x2):
    if fhelper.f(x1) < fhelper.f(x2):
        temp = x1
        x1 = x2
        x2 = temp

    xc = 0.5 * (x1 + x2)
    xr = x1 + (x1 - x2)
    xe = x1 + 2 * (x1 - x2)
    if fhelper.f(xr) > fhelper.f(x1):
        if fhelper.f(xe) > fhelper.f(x1):
            return neldermead(x1, xe)
        else:
            return neldermead(x1, xr)
    else:
        if fhelper.f(x1) - fhelper.f(x2) < 0.01:
            return x1, fhelper.f(x1)
        return neldermead(x1, xc)


if __name__ == '__main__':
    main()
