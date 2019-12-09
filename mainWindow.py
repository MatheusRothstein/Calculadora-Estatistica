
import sys
from math import sqrt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from main import Calculadora as c



class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.line = QLineEdit(self)
        self.line.move(5, 5)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.text()

        zero = QPushButton("moda", self)
        zero.move(5, 265)
        zero.clicked.connect(self.calcularAModa)
        
        one = QPushButton("media", self)
        one.move(5, 215)
        one.clicked.connect(self.calcularAMedia)

        two = QPushButton("mediana", self)
        two.move(90, 215)
        two.clicked.connect(self.calcularAMediana)

        three = QPushButton("variância", self)
        three.move(145, 215)

        four = QPushButton("desvio padrão", self)
        four.move(5, 165)

        five = QPushButton("5", self)
        five.move(60, 165)

        six = QPushButton("6", self)
        six.move(115, 165)

        seven = QPushButton("7", self)
        seven.move(5, 115)

        eight = QPushButton("8", self)
        eight.move(60, 115)

        nine = QPushButton("9", self)
        nine.move(115, 115)


        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 520)
        self.show()

    def getTextAndReturnList(self):
        texto = self.line.text()
        lista = texto.split()
        listaNova = list(map(float, lista))
        return listaNova
        
    def calcularAModa(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        self.function.calculaModa()

    def calcularAMedia(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        self.function.calculaMedia()

    def calcularAMediana(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        self.function.calculaMediana()

    def calcularAVariancia(self):
        pass

        


def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
