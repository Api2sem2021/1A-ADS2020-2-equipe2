import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui
class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        self.caixa_texto = QLineEdit(self)  # caixa de texto
        self.caixa_texto.move(25,20)
        self.caixa_texto.resize(200,30)

        botao1 = QPushButton('print', self)
        botao1.move(150,200)
        botao1.resize(120,80)
        botao1.setStyleSheet('QPushButton {background-color:#5F3992;font:bold;fonte-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botao_caixa = QPushButton('Enviar texto', self)
        botao_caixa.move(550, 200)
        botao_caixa.resize(120, 80)
        botao_caixa.setStyleSheet('QPushButton {background-color:#5F3992;font:bold;fonte-size:20px}')
        botao_caixa.clicked.connect(self.mostra_texto)

        botao2 = QPushButton('botao 2', self)
        botao2.move(350, 200)
        botao2.resize(120, 80)
        botao2.setStyleSheet('QPushButton {background-color:#5F3992;font:bold;fonte-size:20px}')
        botao2.clicked.connect(self.botao2_click)
        self.label1_1 = QLabel(self)
        self.label1_1.setText("Qual comando é utilizado para imprimir uma mensagem na tela?")
        self.label1_1.move(50,50)
        self.label1_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"blue"}')
        self.label1_1.resize(400,25)

        self.label1_caixa = QLabel(self)
        self.label1_caixa.setText("Digitou:")
        self.label1_caixa.move(450, 50)
        self.label1_caixa.setStyleSheet('QLabel {font:bold;font-size:25px;color:"blue"}')
        self.label1_caixa.resize(400, 25)

        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))
        self.carro.resize(450, 200)
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label1_1.setText('Carro 1 selecionado!')
        self.label1_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"red"}')
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label1_caixa.setText(conteudo)


    def botao2_click(self):
        self.label1_1.setText('Carro 2 selecionado!')
        self.label1_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"yellow"}')
        self.carro.setPixmap(QtGui.QPixmap('carro2.png'))


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec())




