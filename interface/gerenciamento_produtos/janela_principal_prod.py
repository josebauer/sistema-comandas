from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from interface.gerenciamento_produtos.janela_cadastro_prod import JanelaCadastroProduto
from interface.gerenciamento_produtos.janela_lista_prod import JanelaListaProdutos
from interface.gerenciamento_produtos.janela_edicao_prod import JanelaEdicaoProduto

class JanelaPrincipalProdutos(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Gerenciar Produtos")
    self.setGeometry(100, 100, 400, 300)

    layout = QVBoxLayout()

    botao_cadastrar = QPushButton("Cadastrar novo produto")
    botao_listar = QPushButton("Ver produtos cadastrados")
    botao_editar = QPushButton("Editar produto")
    botao_sair = QPushButton("Sair")
    
    botao_cadastrar.setFixedHeight(50)
    botao_listar.setFixedHeight(50)
    botao_editar.setFixedHeight(50)
    botao_sair.setFixedHeight(50)

    botao_cadastrar.clicked.connect(self.abrir_janela_cadastro)
    botao_listar.clicked.connect(self.abrir_janela_lista)
    botao_editar.clicked.connect(self.abrir_janela_edicao)
    botao_sair.clicked.connect(self.close)

    layout.addWidget(botao_cadastrar)
    layout.addWidget(botao_listar)
    layout.addWidget(botao_editar)
    layout.addWidget(botao_sair)

    self.setLayout(layout)

  def abrir_janela_cadastro(self):
    self.janela_cadastro = JanelaCadastroProduto()
    self.janela_cadastro.show()

  def abrir_janela_lista(self):
    self.janela_lista = JanelaListaProdutos()
    self.janela_lista.show()

  def abrir_janela_edicao(self):
    self.janela_edicao = JanelaEdicaoProduto()
    self.janela_edicao.show()