from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from data.usuarios import usuarios

class JanelaListaUsuarios(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Usuários Cadastrados")
    self.setGeometry(300, 300, 400, 300)

    layout = QVBoxLayout()

    titulo = QLabel("Usuários Cadastrados")
    titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
    layout.addWidget(titulo)

    self.lista = QListWidget()
    self.carregar_usuarios()
    layout.addWidget(self.lista)

    btn_fechar = QPushButton("Fechar")
    btn_fechar.clicked.connect(self.close)
    layout.addWidget(btn_fechar)
    btn_fechar.setFixedHeight(50)

    self.setLayout(layout)

  def carregar_usuarios(self):
    self.lista.clear()
    if not usuarios:
      self.lista.addItem("Nenhum usuário cadastrado.")
    else:
      for usuario in usuarios:
        self.lista.addItem(f"{usuario.nome} - {usuario.funcao}")