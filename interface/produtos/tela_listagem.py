from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from data.produtos import produtos

class TelaListagem(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Produtos Cadastrados")
    self.setGeometry(300, 300, 400, 300)

    layout = QVBoxLayout()

    titulo = QLabel("Produtos Cadastrados")
    titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
    layout.addWidget(titulo)

    self.lista = QListWidget()
    self.carregar_produtos()
    layout.addWidget(self.lista)

    btn_voltar = QPushButton("Voltar")
    btn_voltar.clicked.connect(self.close)
    layout.addWidget(btn_voltar)
    btn_voltar.setFixedHeight(50)

    self.setLayout(layout)

  def carregar_produtos(self):
    self.lista.clear()
    if not produtos:
      self.lista.addItem("Nenhum produto cadastrado.")
    else:
      for produto in produtos:
        self.lista.addItem(f"{produto.nome} | Valor: R${produto.valor} | Disponível: {'Sim' if produto.disponibilidade else 'Não'}")