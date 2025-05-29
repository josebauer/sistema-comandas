from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from interface.produtos.tela_cadastro import TelaCadastro 
from interface.produtos.tela_listagem import TelaListagem
from interface.produtos.tela_edicao import TelaEdicao

class TelaPrincipalProdutos(QWidget):
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

    botao_cadastrar.clicked.connect(self.mostrar_tela_cadastro)
    botao_listar.clicked.connect(self.mostrar_tela_lista)
    botao_editar.clicked.connect(self.mostrar_tela_edicao)
    botao_sair.clicked.connect(self.close)

    layout.addWidget(botao_cadastrar)
    layout.addWidget(botao_listar)
    layout.addWidget(botao_editar)
    layout.addWidget(botao_sair)

    self.setLayout(layout)

  def mostrar_tela_cadastro(self):
    self.janela_cadastro = TelaCadastro()
    self.janela_cadastro.show()

  def mostrar_tela_lista(self):
    self.janela_lista = TelaListagem()
    self.janela_lista.show()

  def mostrar_tela_edicao(self):
    self.janela_edicao = TelaEdicao()
    self.janela_edicao.show()