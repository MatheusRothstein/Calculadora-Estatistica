from random import randint
from math import sqrt
import statistics


class Calculadora:
    def __init__(self, listaValores):
        self.listaValores = listaValores

    def is_impar(self, num):
        if (num % 2) != 0:
            return True
        return False

    def calculaMedia(self):
        return sum(self.listaValores) / len(self.listaValores)

    def calculaMediana(self):
        numeros_ordenados = sorted(self.listaValores)
        if self.is_impar(len(numeros_ordenados)):
            meio = int(len(numeros_ordenados) / 2)
            return numeros_ordenados[meio]
        meio_cima = int(round(len(numeros_ordenados) / 2 + 0.5))
        meio_baixo = int(round(len(numeros_ordenados) / 2))
        return (numeros_ordenados[meio_cima] + numeros_ordenados[meio_baixo]) / 2

    def calculaModa(self):
        ocorrencias = {}
        moda = []
        for item in self.listaValores:
            if item not in ocorrencias:
                ocorrencias[item] = self.listaValores.count(item)
        for k, v in ocorrencias.items():
            if not moda:
                moda.append(k)
            else:
                if v > ocorrencias[moda[-1]]:
                    moda = [k]
                elif v == ocorrencias[moda[-1]]:
                    moda.append(k)
        if len(moda) > 1:
            m = abs(self.calculaMedia() - moda[0])
            moda_atualizada = [moda[0]]
            for valor in moda[1:]:
                if abs(self.calculaMedia() - valor) < m:
                    m = abs(self.calculaMedia() - valor)
                    moda_atualizada = valor
            moda = [moda_atualizada]

        return moda[0]

    def calculaVariancia(self):
        media = self.calculaMedia()
        var = 0
        variance = 0
        for item in self.listaValores:
            var += ((item - media) ** 2)
        variance = var / (len(self.listaValores))
        return variance

    def calculaVariancia_amostral(self):
        media = self.calculaMedia()
        var = 0
        variance_pop = 0
        for item in self.listaValores:
            var += ((item - media) ** 2)
        variance_pop = var / (len(self.listaValores) - 1)
        return variance_pop

    def calculaDesvioPadrao(self):
        return sqrt(self.calculaVariancia())

    def divisao_classes(self):
        qtd_classes = int(round(sqrt(len(self.listaValores)) + 0.5))
        amplitude = round((max(self.listaValores) - min(self.listaValores)) // qtd_classes + 0.5)
        classes = {}
        count = int(min(self.listaValores))
        for k in range(0, qtd_classes + 1):
            if count > max(self.listaValores):
                break
            classes[(count, count + amplitude)] = 0
            count += amplitude
        for item in self.listaValores:
            for k, v in classes.items():
                minimo, maximo = k
                if item >= minimo and item < maximo:
                    classes[(minimo, maximo)] += 1
        return classes

    def formata_divisao_classes(self):
        texto = ''
        for k, v in self.divisao_classes().items():
            menor, maior = k
            texto += f'{menor} |- {maior} = {v}\n'
        return texto

    def cria_labels_values(self):
        labels = []
        values = []
        for k, v in self.divisao_classes().items():
            menor, maior = k
            labels.append(f'{menor} |- {maior}')
            values.append(v)
        return (labels, values)


if __name__ == "__main__":
    valores_aleatorios = [float(randint(1, 100)) for x in range(1, 11)]
    calculo = Calculadora(listaValores=valores_aleatorios)
    print("nossa media", calculo.calculaMedia())
    print("statics", statistics.mean(valores_aleatorios))
    print("nossa mediana", calculo.calculaMediana())
    print("statistics mediana", statistics.median(valores_aleatorios))
    print("nossa moda", calculo.calculaModa())
    print("statitics moda", statistics.mode(valores_aleatorios))
    print("nossa variancia", calculo.calculaVariancia())
    print("statistics variancia", statistics.variance(valores_aleatorios))
    print("nosso desvio padrao", calculo.calculaDesvioPadrao())
    print("statistics desvio padrao", statistics.stdev(valores_aleatorios))
    print(valores_aleatorios)
    print("DIVISÃO POR CLASSE", calculo.divisao_classes())
    print("_____________\n%s" % calculo.formata_divisao_classes())
