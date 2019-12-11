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

    fig.savefig('distribuicao_classe')
