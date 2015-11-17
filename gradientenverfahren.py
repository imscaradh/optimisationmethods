from functionhelper.function import df
from functionhelper.plotter import graph


def main():
    graph("10 * x ** 4 - 17 * x ** 3 - 67 * x ** 2 / 10 + 253 * x / 20 - 107 / 50", range(-100, 100))

    lmbda = 0.001
    df_result = 1
    point = -5
    while abs(df_result) > 0.0001:
        df_result = df(point)
        point -= lmbda * df_result

    print(point)


if __name__ == '__main__':
    main()
