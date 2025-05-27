from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from interface.gerenciamento_usuario.janela_principal import JanelaPrincipal
from interface.pedidos.janela_pedidos import JanelaPedidos
from data.usuarios import usuarios

class JanelaLogin(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Login")
    self.setGeometry(100, 100, 400, 250)

    layout = QVBoxLayout()

    self.email_input = QLineEdit()
    self.email_input.setPlaceholderText("Email")
    self.email_input.setFixedHeight(50)

    self.senha_input = QLineEdit()
    self.senha_input.setPlaceholderText("Senha")
    self.senha_input.setEchoMode(QLineEdit.Password)
    self.senha_input.setFixedHeight(50)

    self.botao_login = QPushButton("Entrar")
    self.botao_login.clicked.connect(self.fazer_login)
    self.botao_login.setFixedHeight(50)

    layout.addWidget(QLabel("Login"))
    layout.addWidget(self.email_input)
    layout.addWidget(self.senha_input)
    layout.addWidget(self.botao_login)

    self.setLayout(layout)

  def fazer_login(self):
    email = self.email_input.text()
    senha = self.senha_input.text()

    for usuario in usuarios:
      if usuario.email == email and usuario.senha == senha:
        self.close()
        if usuario.funcao == "Administrador":
          self.janela_principal = JanelaPrincipal()
          self.janela_principal.show()
          return
        else:
          self.janela_pedidos = JanelaPedidos()
      QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")