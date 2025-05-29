from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox, QMessageBox, QCheckBox
from classes.usuario import Usuario
from data.produtos import produtos

categorias = ["Sobremesa", "Torta"]

class TelaCadastro(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Cadastro de Usuário")
    self.setGeometry(150, 150, 400, 250)

    layout = QFormLayout()

    self.input_nome = QLineEdit()
    self.input_nome.setFixedHeight(50)
    self.input_valor = QLineEdit()
    self.input_valor.setFixedHeight(50)
    self.input_descricao = QLineEdit()
    self.input_descricao.setFixedHeight(50)
    self.checkbox_disponivel = QCheckBox("Disponível")
    self.checkbox_disponivel.setChecked(True)

    self.combo_categoria = QComboBox()
    self.combo_categoria.addItems(categorias)
    self.combo_categoria.setFixedHeight(50)

    self.botao_cadastrar = QPushButton("Cadastrar")
    self.botao_cadastrar.clicked.connect(self.cadastrar_produto)
    self.botao_cadastrar.setFixedHeight(50)

    layout.addRow("Nome do produto:", self.input_nome)
    layout.addRow("Valor:", self.input_valor)
    layout.addRow("Descrição:", self.input_descricao)
    layout.addRow("Disponivel:", self.checkbox_disponivel)
    layout.addRow("Categoria:", self.combo_categoria)
    layout.addRow(self.botao_cadastrar)

    self.setLayout(layout)

  def cadastrar_produto(self):
    nome = self.input_nome.text().strip()
    valor = self.input_valor.text().strip()
    descricao = self.input_descricao.text().strip()
    disponibilidade = self.checkbox_disponivel.isChecked()
    categoria = self.combo_categoria.currentText()

    if not nome or not valor or not descricao or not categoria:
      QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
      return

    novo_produto = Usuario(nome, valor, descricao, disponibilidade, categoria)
    produtos.append(novo_produto)
    QMessageBox.information(self, "Sucesso", "Produto cadastrado com sucesso!")

    self.close()