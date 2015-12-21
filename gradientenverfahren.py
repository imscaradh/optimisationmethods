import functionhelper.function as fhelper
from functionhelper.plotter import graph


def main():

    fhelper.func = (input("Enter function: "))

    lmbda = 0.001
    point = -5
    df_result = fhelper.df(point)
    while abs(df_result) > 0.0001:
        df_result = fhelper.df(point)
        point -= lmbda * df_result

    print(point)


if __name__ == '__main__':
    main()
