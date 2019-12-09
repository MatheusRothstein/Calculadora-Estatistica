
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

        zero = QPushButton("moda", self)
        zero.move(5, 285)
        zero.clicked.connect(self.calcularAModa)
        
        one = QPushButton("media", self)
        one.move(5, 235)
        one.clicked.connect(self.calcularAMedia)

        two = QPushButton("mediana", self)
        two.move(155, 235)
        two.clicked.connect(self.calcularAMediana)

        three = QPushButton("variância", self)
        three.move(300, 235)
        three.clicked.connect(self.calcularAVariancia)

        four = QPushButton("desvio padrão", self)
        four.move(5, 185)
        four.clicked.connect(self.calcularDesvioPadrao)

        five = QPushButton("Divisão de classes", self)
        five.move(155, 185)
        five.clicked.connect(self.calculaDivisaoDeClasses)

        six = QPushButton("6", self)
        six.move(300, 185)

        seven = QPushButton("7", self)
        seven.move(5, 135)

        eight = QPushButton("8", self)
        eight.move(155, 135)

        nine = QPushButton("9", self)
        nine.move(300, 135)


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
        result = self.function.calculaModa()
        self.answer.setText(str(result))

    def calcularAMedia(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        resultado = self.function.calculaMedia()
        self.answer.setText(str(resultado))

    def calcularAMediana(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        resultado = self.function.calculaMediana()
        self.answer.setText(str(resultado))

    def calcularAVariancia(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        resultado = self.function.calculaVariancia()
        self.answer.setText(str(resultado))

    def calcularDesvioPadrao(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        resultado = self.function.calculaDesvioPadrao()
        self.answer.setText(str(int(resultado)))

    def calculaDivisaoDeClasses(self):
        lista = self.getTextAndReturnList()
        self.function = c(lista)
        resultado = self.function.formata_divisao_classes()
        self.answer.setText(resultado)



def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
