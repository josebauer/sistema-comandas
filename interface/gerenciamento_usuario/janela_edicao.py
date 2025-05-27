from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox, QMessageBox
from data.usuarios import usuarios

class JanelaEdicao(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Editar Usuário")
    self.setGeometry(150, 150, 400, 300)

    self.layout = QFormLayout()

    self.input_cpf_busca = QLineEdit()
    self.input_cpf_busca.setFixedHeight(50)
    self.botao_buscar = QPushButton("Buscar")
    self.botao_buscar.clicked.connect(self.buscar_usuario)
    self.botao_buscar.setFixedHeight(40)

    self.input_nome = QLineEdit()
    self.input_nome.setFixedHeight(50)
    self.input_email = QLineEdit()
    self.input_email.setFixedHeight(50)
    self.input_senha = QLineEdit()
    self.input_senha.setFixedHeight(50)
    self.input_funcao = QComboBox()
    self.input_funcao.addItems(["Atendente", "Administrador"])
    self.input_funcao.setFixedHeight(50)
    self.botao_salvar = QPushButton("Salvar alterações")
    self.botao_salvar.clicked.connect(self.salvar_edicao)
    self.botao_salvar.setEnabled(False)
    self.botao_salvar.setFixedHeight(50)

    self.layout.addRow("CPF do usuário:", self.input_cpf_busca)
    self.layout.addRow(self.botao_buscar)
    self.layout.addRow("Nome:", self.input_nome)
    self.layout.addRow("Email:", self.input_email)
    self.layout.addRow("Senha:", self.input_senha)
    self.layout.addRow("Função:", self.input_funcao)
    self.layout.addRow(self.botao_salvar)

    self.setLayout(self.layout)
    self.usuario_encontrado = None

  def buscar_usuario(self):
    cpf_texto = self.input_cpf_busca.text().strip()

    try:
      cpf = int(cpf_texto)
    except ValueError:
      QMessageBox.warning(self, "Erro", "CPF inválido.")
      return

    for usuario in usuarios:
      if usuario.cpf == cpf:
        self.usuario_encontrado = usuario
        self.input_nome.setText(usuario.nome)
        self.input_email.setText(usuario.email)
        self.input_senha.setText(usuario.senha)
        self.input_funcao.setCurrentText(usuario.funcao)
        self.botao_salvar.setEnabled(True)
        return

    QMessageBox.information(self, "Não encontrado", "Usuário não encontrado.")

  def salvar_edicao(self):
    if not self.usuario_encontrado:
      return

    self.usuario_encontrado.nome = self.input_nome.text().strip()
    self.usuario_encontrado.email = self.input_email.text().strip()
    self.usuario_encontrado.senha = self.input_senha.text().strip()
    self.usuario_encontrado.funcao = self.input_funcao.currentText()

    QMessageBox.information(self, "Sucesso", "Usuário atualizado com sucesso.")
    self.close()