from random import randint


class CalculadoraEstatistica:
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
            meio = len(numeros_ordenados) / 2
            return numeros_ordenados[meio]
        meio_cima = round(len(numeros_ordenados) + 0.5)
        meio_baixo = round(len(numeros_ordenados) - 0.5)
        return (numeros_ordenados[meio_cima] + numeros_ordenados[meio_baixo]) / 2


if __name__ == "__main__":
    valores_aleatorios = [randint(1, 10) for x in range(1, 10)]
    calculo = CalculadoraEstatistica(listaValores=valores_aleatorios)
    print(calculo.calculaMedia())
    print(calculo.calculaMediana())
    print(4.5 // 2)