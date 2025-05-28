from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from interface.janela_gerenciamento import JanelaGerenciamento
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
    self.email_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 10px")

    self.senha_input = QLineEdit()
    self.senha_input.setPlaceholderText("Senha")
    self.senha_input.setEchoMode(QLineEdit.Password)
    self.senha_input.setFixedHeight(50)
    self.senha_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 10px")

    self.botao_login = QPushButton("Entrar")
    self.botao_login.clicked.connect(self.fazer_login)
    self.botao_login.setStyleSheet("color: white; background-color: #1aac3f; font-weight: bold; margin-top: 10px; border-radius: 10px")
    self.botao_login.setFixedHeight(50)

    label_boas_vindas = QLabel("Bem vindo! Insira suas credenciais abaixo:")
    label_boas_vindas.setStyleSheet("font-size: 14px; text-align: center")
    layout.addWidget(label_boas_vindas)
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
          self.janela_principal = JanelaGerenciamento()
          self.janela_principal.show()
          return
        else:
          self.janela_pedidos
      QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")