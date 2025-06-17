import customtkinter as ctk
from tkinter import messagebox
from interface.pedidos.tela_cadastro import TelaCadastroPedido
from data.produtos import listar_produtos

class TelaPrincipalPedidos(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.trocar_tela_callback = trocar_tela_callback
    self.usuario = usuario

    frame = ctk.CTkFrame(self, fg_color="transparent")
    frame.pack(expand=True)

    titulo = ctk.CTkLabel(frame, text="Gerenciar Cardápio", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 20))

    # --- Botão para cadastrar um pedido
    botao_cadastrar = ctk.CTkButton(
      frame,
      text="Cadastrar novo pedido",
      command=self.mostrar_tela_cadastro,
      height=45,
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )

    #--- Botão para listar os produtos cadastrados
    botao_listar = ctk.CTkButton(
      frame,
      text="Pedidos realizados",
      command=self.mostrar_tela_listar,
      height=45,
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )

    #--- Botão para voltar a tela  anterior
    botao_voltar = ctk.CTkButton(
      frame,
      text="Voltar",
      command=self.voltar,
      height=45,
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#63a9ff",
      hover_color="#63a9ff",
      font=ctk.CTkFont(size=14, weight="bold")
    )

    botao_cadastrar.pack(pady=10, fill="x")
    botao_listar.pack(pady=10, fill="x")
    botao_voltar.pack(pady=10, fill="x")

  #--- Função para mostrar a tela de cadastro do produto
  def mostrar_tela_cadastro(self):
    self.produtos = listar_produtos()

    if self.produtos:
      self.trocar_tela_callback(TelaCadastroPedido, self.usuario)
    else:
      messagebox.showwarning("Atenção", "Ainda não há produtos cadastrados.")
      from interface.produtos.tela_principal import TelaPrincipalProdutos
      self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario)
    
    
  #--- Função para mostrar a tela de listagem dos produtos cadastrados
  def mostrar_tela_listar(self):
    # self.trocar_tela_callback(TelaListagemProduto, self.usuario)
    pass

  #--- Função para voltar a tela anterior
  def voltar(self):
    from interface.tela_gerenciamento import TelaGerenciamento
    self.trocar_tela_callback(TelaGerenciamento, self.usuario)