from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from interface.gerenciamento_usuario.janela_principal_usuarios import JanelaPrincipalUsuarios
from interface.gerenciamento_produtos.janela_principal_prod import JanelaPrincipalProdutos

class JanelaGerenciamento(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Gerenciamento")
    self.setGeometry(100, 100, 400, 300)

    layout = QVBoxLayout()
    
    botao_geren_usuarios = QPushButton("Gerenciar usuários")
    botao_geren_produtos = QPushButton("Gerenciar produtos")
    botao_geren_pedidos = QPushButton("Gerenciar pedidos")
    botao_sair = QPushButton("Sair")
    
    botao_geren_usuarios.setFixedHeight(50)
    botao_geren_produtos.setFixedHeight(50)
    botao_geren_pedidos.setFixedHeight(50)
    botao_sair.setFixedHeight(50)

    botao_geren_usuarios.clicked.connect(self.abrir_janela_usuarios)
    botao_geren_produtos.clicked.connect(self.abrir_janela_produtos)
    botao_geren_pedidos.clicked.connect(self.abrir_janela_pedidos)
    botao_sair.clicked.connect(self.close)

    layout.addWidget(botao_geren_usuarios)
    layout.addWidget(botao_geren_produtos)
    layout.addWidget(botao_geren_pedidos)
    layout.addWidget(botao_sair)

    self.setLayout(layout)

  def abrir_janela_usuarios(self):
    self.janela_principal_usuario = JanelaPrincipalUsuarios()
    self.janela_principal_usuario.show()

  def abrir_janela_produtos(self):
    self.janela_principal_produtos = JanelaPrincipalProdutos()
    self.janela_principal_produtos.show()

  def abrir_janela_pedidos(self):
    # self.janela_consulta = JanelaConsulta()
    # self.janela_consulta.show()
    pass
