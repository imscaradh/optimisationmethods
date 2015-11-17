from functionhelper.function import f, df


def main():
    x = -10
    deviation = 1
    while abs(deviation) > 0.01:
        deviation = df(x)
        if deviation > 0.01:
            x += 0.0001
        else:
            x -= 0.0001

    print(x)


if __name__ == '__main__':
    main()
