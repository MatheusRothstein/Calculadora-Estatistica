import matplotlib.pyplot as plt
import numpy as np


def grafico_barra_distribuicao_classes(labels, values):
    objects = labels
    y_pos = np.arange(len(objects))
    performance = values

    fig = plt.figure()
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Valor absoluto')
    plt.title('Distribuição por classes')

    fig.savefig('distribuicao_classe.png')

    return fig


def estimate_coef(x, y):
    n = np.size(x)

    m_x, m_y = np.mean(x), np.mean(y)

    SS_xy = np.sum(y * x - n * m_y * m_x)
    SS_xx = np.sum(x * x - n * m_x * m_x)

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(xs, ys):
    dev = estimate_coef(xs, ys)

    y_pred = []
    for x in xs:
        y_pred.append(dev[0] + dev[1] * x)
    plt.plot(xs, y_pred, color="g")


def grafico_regressao(xarr, yarr):
    x = np.array(xarr)
    y = np.array(yarr)

    fig = plt.figure()

    plt.scatter(x, y)

    plot_regression_line(x, y)

    fig.savefig('regressao.png')
    return fig


if __name__ == "__main__":
    xarr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    yarr = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
    grafico_regressao(xarr, yarr)