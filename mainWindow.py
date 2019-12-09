import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from random import randint

from main import Calculadora


class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()
        self.calculadora = Calculadora(listaValores=self.getTextAndReturnList())

    def initUI(self):
        self.line = QLineEdit(self)
        self.line.move(5, 5)
        self.line.setAlignment(Qt.AlignLeft)
        self.line.resize(390, 100)
        font = self.line.font()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.text()

        self.answer = QTextEdit(self)
        self.answer.setReadOnly(True)
        self.answer.move(5, 350)
        self.answer.resize(390, 160)

        self.myLabel = QLabel(self)
        self.myLabel.setText("Resultado: ")
        self.myLabel.move(5, 325)
        self.myLabel.setFont(font)

        self.qtd = QLineEdit(self)
        self.qtd.move(20, 115)
        self.qtd.resize(60, 30)
        self.qtd.setPlaceholderText("Qtd")
        self.qtd.setStyleSheet("background-color: rgb(255, 0, 0, 0.5);")

        self.menor = QLineEdit(self)
        self.menor.move(110, 115)
        self.menor.resize(60, 30)
        self.menor.setPlaceholderText("Menor")
        self.menor.setStyleSheet("background-color: rgb(255, 0, 0, 0.5);")

        self.maior = QLineEdit(self)
        self.maior.move(200, 115)
        self.maior.resize(60, 30)
        self.maior.setPlaceholderText("Maior")
        self.maior.setStyleSheet("background-color: rgb(255, 0, 0, 0.5);")

        gerar = QPushButton("Gerar Valores", self)
        gerar.move(290, 115)
        gerar.clicked.connect(self.gerar_valores)
        gerar.setStyleSheet("background-color: red")

        media = QPushButton("Média", self)
        media.move(5, 200)
        media.clicked.connect(self.calcularAMedia)
        media.setStyleSheet("background-color: blue")

        mediana = QPushButton("Mediana", self)
        mediana.move(150, 200)
        mediana.clicked.connect(self.calcularAMediana)
        mediana.setStyleSheet("background-color: blue")

        moda = QPushButton("Moda", self)
        moda.move(295, 200)
        moda.clicked.connect(self.calcularAModa)
        moda.setStyleSheet("background-color: blue")

        dpadrao = QPushButton("Desvio Padrão", self)
        dpadrao.move(5, 250)
        dpadrao.clicked.connect(self.calcularDesvioPadrao)
        dpadrao.setStyleSheet("background-color: blue")

        variancia = QPushButton("Variância", self)
        variancia.move(150, 250)
        variancia.clicked.connect(self.calcularAVariancia)
        variancia.setStyleSheet("background-color: blue")

        distribuicao = QPushButton("Distribuição", self)
        distribuicao.move(295, 250)
        distribuicao.clicked.connect(self.calculaDivisaoDeClasses)
        distribuicao.setStyleSheet("background-color: blue")

        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle("Calculadora Estatística")
        self.setFixedSize(400, 520)
        self.show()

    def gerar_valores(self):
        texto = ''
        for k in range(0, int(self.qtd.text())):
            texto += ('%s ' % randint(int(self.menor.text()), int(self.maior.text())))
        self.line.setText(texto)

    def getTextAndReturnList(self):
        texto = self.line.text()
        lista = texto.split()
        listaNova = list(map(float, lista))
        return listaNova

    def calcularAModa(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        result = self.calculadora.calculaModa() or 'Sem valores'
        self.answer.setText(str(result))

    def calcularAMedia(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaMedia() or 'Sem valores'
        self.answer.setText(str(resultado))

    def calcularAMediana(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaMediana() or 'Sem valores'
        self.answer.setText(str(resultado))

    def calcularAVariancia(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaVariancia() or 'Sem valores'
        self.answer.setText(str(resultado))

    def calcularDesvioPadrao(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaDesvioPadrao() or 'Sem valores'
        self.answer.setText(str(int(resultado)))

    def calculaDivisaoDeClasses(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.formata_divisao_classes() or 'Sem valores'
        self.answer.setText(resultado)


def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
