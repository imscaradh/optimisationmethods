import matplotlib.pyplot as plt


def graph(formula, x_range, x_label, y_label, name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_range, [formula(value) for value in x_range])
    plt.grid(True)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig("%s.png" % name)
