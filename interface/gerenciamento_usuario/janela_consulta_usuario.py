from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from data.usuarios import usuarios

class JanelaConsultaUsuario(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Consultar Usuário por CPF")
    self.setGeometry(150, 150, 400, 200)

    layout = QVBoxLayout()

    self.input_cpf = QLineEdit()
    self.input_cpf.setPlaceholderText("Digite o CPF (apenas números)")
    self.input_cpf.setFixedHeight(50)
    self.botao_consultar = QPushButton("Consultar")
    self.botao_consultar.setFixedHeight(50)
    self.resultado = QLabel("")

    self.botao_consultar.clicked.connect(self.consultar_usuario)

    layout.addWidget(self.input_cpf)
    layout.addWidget(self.botao_consultar)
    layout.addWidget(self.resultado)

    self.setLayout(layout)

  def consultar_usuario(self):
    cpf_texto = self.input_cpf.text().strip()

    try:
      cpf = int(cpf_texto)
    except ValueError:
      QMessageBox.warning(self, "Erro", "CPF inválido.")
      return

    for usuario in usuarios:
      if usuario.cpf == cpf:
          self.resultado.setText(
              f"Nome: {usuario.nome}\n"
              f"Email: {usuario.email}\n"
              f"Função: {usuario.funcao}"
          )
          return

    QMessageBox.information(self, "Não encontrado", "Usuário não encontrado.")