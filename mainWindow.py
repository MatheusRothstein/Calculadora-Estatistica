import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from random import randint

from main import Calculadora
from graficos import grafico_barra_distribuicao_classes as graph


class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()
        self.calculadora = Calculadora(listaValores=self.getTextAndReturnList())
        self.calc2 = Calculadora(listaValores=self.getTextAndReturnList2())

    def initUI(self):

        self.line = QLineEdit(self)
        self.line.move(5, 5)
        self.line.setAlignment(Qt.AlignLeft)
        self.line.resize(390, 50)
        font = self.line.font()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.text()

        self.line2 = QLineEdit(self)
        self.line2.move(5, 60)
        self.line2.setAlignment(Qt.AlignLeft)
        self.line2.resize(390, 50)
        font = self.line2.font()
        font.setPointSize(12)
        self.line2.setFont(font)
        self.line2.text()

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

        self.gerar = QPushButton("Gerar Valores", self)
        self.gerar.move(290, 115)
        self.gerar.clicked.connect(self.gerar_valores)
        self.gerar.setStyleSheet("background-color: red")

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
        distribuicao.clicked.connect(self.distri)
        distribuicao.setStyleSheet("background-color: blue")

        regressao = QPushButton("Regressão", self)
        regressao.move(5, 300)
        regressao.setStyleSheet("background-color: blue")

        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle("Calculadora Estatística")

        self.setFixedSize(1000, 520)
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
    
    def getTextAndReturnList2(self):
        texto2 = self.line2.text()
        lista2 = texto2.split()
        listaNova2 = list(map(float, lista2))
        return listaNova2

    def calcularAModa(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        result = self.calculadora.calculaModa() or 'Sem valores'

        self.calc2.listaValores = self.getTextAndReturnList2()
        result2 = self.calc2.calculaModa() or "Sem valores"

        resposta = "Moda grupo 1: %s\nModa grupo 2: %s" % (str(result), str(result2))

        self.answer.setText(str(resposta))

    def showGraph(self, imagem):
        self.labelTeste = QLabel(self)
        self.labelTeste.move(400, 5)
        self.labelTeste.setVisible(True)
        pixmap = QPixmap(imagem)
        self.labelTeste.setPixmap(pixmap)
        self.labelTeste.resize(pixmap.width(), pixmap.height())

    def calcularAMedia(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaMedia() or 'Sem valores'

        self.calc2.listaValores = self.getTextAndReturnList2()
        result2 = self.calc2.calculaMedia()

        resposta = "Média grupo 1: %s\nMédia grupo 2: %s" % (str(resultado), str(result2))
        self.answer.setText(str(resposta))

    def calcularAMediana(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaMediana() or 'Sem valores'

        self.calc2.listaValores = self.getTextAndReturnList2()
        result2 = self.calc2.calculaMediana()

        resposta = "Mediana grupo 1: %s\nMediana grupo 2: %s" % (str(resultado), str(result2))
        self.answer.setText(str(resposta))

    def calcularAVariancia(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaVariancia() or 'Sem valores'

        self.calc2.listaValores = self.getTextAndReturnList2()
        result2 = self.calc2.calculaVariancia()

        resposta = "Variância grupo 1: %s\nVariância grupo 2: %s" % (str(resultado), str(result2))
        self.answer.setText(str(resposta))

    def calcularDesvioPadrao(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.calculaDesvioPadrao() or 'Sem valores'

        self.calc2.listaValores = self.getTextAndReturnList2()
        resultado2 = self.calc2.calculaDesvioPadrao()
 
        resposta = "Desv. Padrão grupo 1: %s\nDesv. Padrão grupo 2: %s" % (str(resultado), str(resultado2))

        self.answer.setText(str(resposta))

    def calculaDivisaoDeClasses(self):
        self.calculadora.listaValores = self.getTextAndReturnList()
        resultado = self.calculadora.formata_divisao_classes() or 'Sem valores'

        self.calc2.listaValores = self.getTextAndReturnList2()
        result2 = self.calc2.divisao_classes()
        
        resposta = "Classes grupo 1: %s\nClasses grupo 2: %s" % (str(resultado), str(result2))
        
        self.answer.setText(str(resposta))

    def distri(self):
        self.calculadora.listaValores = self.getTextAndReturnList()   
        self.calculaDivisaoDeClasses()

        info = self.calculadora.cria_labels_values()
        label = info[0]
        value = info[1]
        self.grafico = graph(label, value)
        self.showGraph('distribuicao_classe.png')
        

def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
