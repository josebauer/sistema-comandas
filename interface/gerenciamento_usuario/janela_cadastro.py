from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox, QMessageBox
from classes.usuario import Usuario
from data.usuarios import usuarios

class JanelaCadastro(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Cadastro de Usuário")
    self.setGeometry(150, 150, 400, 250)

    layout = QFormLayout()

    self.input_nome = QLineEdit()
    self.input_nome.setFixedHeight(50)
    self.input_cpf = QLineEdit()
    self.input_cpf.setFixedHeight(50)
    self.input_email = QLineEdit()
    self.input_email.setFixedHeight(50)
    self.input_senha = QLineEdit()
    self.input_senha.setEchoMode(QLineEdit.Password)
    self.input_senha.setFixedHeight(50)

    self.combo_funcao = QComboBox()
    self.combo_funcao.addItems(["Atendente", "Administrador"])
    self.combo_funcao.setFixedHeight(50)

    self.botao_cadastrar = QPushButton("Cadastrar")
    self.botao_cadastrar.clicked.connect(self.cadastrar_usuario)
    self.botao_cadastrar.setFixedHeight(50)

    layout.addRow("Nome completo:", self.input_nome)
    layout.addRow("CPF (somente números):", self.input_cpf)
    layout.addRow("Email:", self.input_email)
    layout.addRow("Senha:", self.input_senha)
    layout.addRow("Função:", self.combo_funcao)
    layout.addRow(self.botao_cadastrar)

    self.setLayout(layout)

  def cadastrar_usuario(self):
    nome = self.input_nome.text().strip()
    cpf_texto = self.input_cpf.text().strip()
    email = self.input_email.text().strip()
    senha = self.input_senha.text().strip()
    funcao = self.combo_funcao.currentText()

    if not nome or not cpf_texto or not email or not senha:
      QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
      return

    try:
      cpf = int(cpf_texto)
    except ValueError:
      QMessageBox.warning(self, "Erro", "CPF deve conter apenas números.")
      return

    for u in usuarios:
      if u.cpf == cpf:
          QMessageBox.warning(self, "Erro", "CPF já cadastrado.")
          return

    novo_usuario = Usuario(nome, cpf, email, senha, funcao)
    usuarios.append(novo_usuario)
    QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")

    self.close()  # Fecha a janela após cadastro