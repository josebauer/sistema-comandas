from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from gui.janela_cadastro import JanelaCadastro
from gui.janela_lista import JanelaListaUsuarios
from gui.janela_consulta import JanelaConsulta
from gui.janela_edicao import JanelaEdicao

class JanelaPrincipal(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Sistema de Gerenciamento de Usuários")
    self.setGeometry(100, 100, 400, 300)

    layout = QVBoxLayout()

    botao_cadastrar = QPushButton("Cadastrar novo usuário")
    botao_listar = QPushButton("Listar todos os usuários")
    botao_consultar = QPushButton("Consultar por CPF")
    botao_editar = QPushButton("Editar usuário")
    botao_sair = QPushButton("Sair")
    
    botao_cadastrar.setFixedHeight(50)
    botao_listar.setFixedHeight(50)
    botao_consultar.setFixedHeight(50)
    botao_editar.setFixedHeight(50)
    botao_sair.setFixedHeight(50)

    botao_cadastrar.clicked.connect(self.abrir_janela_cadastro)
    botao_listar.clicked.connect(self.abrir_janela_lista)
    botao_consultar.clicked.connect(self.abrir_janela_consulta)
    botao_editar.clicked.connect(self.abrir_janela_edicao)
    botao_sair.clicked.connect(self.close)

    layout.addWidget(botao_cadastrar)
    layout.addWidget(botao_listar)
    layout.addWidget(botao_consultar)
    layout.addWidget(botao_editar)
    layout.addWidget(botao_sair)

    self.setLayout(layout)

  def abrir_janela_cadastro(self):
    self.janela_cadastro = JanelaCadastro()
    self.janela_cadastro.show()

  def abrir_janela_lista(self):
    self.janela_lista = JanelaListaUsuarios()
    self.janela_lista.show()

  def abrir_janela_consulta(self):
    self.janela_consulta = JanelaConsulta()
    self.janela_consulta.show()

  def abrir_janela_edicao(self):
    self.janela_edicao = JanelaEdicao()
    self.janela_edicao.show()