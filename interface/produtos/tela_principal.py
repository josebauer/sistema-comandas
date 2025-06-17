import customtkinter as ctk
from tkinter import messagebox
from data.categorias import listar_categorias
from interface.categorias.tela_cadastro import TelaCadastroCategoria
from interface.categorias.tela_listagem import TelaListagemCategoria
from interface.produtos.tela_cadastro import TelaCadastroProduto
from interface.produtos.tela_listagem import TelaListagemProduto

class TelaPrincipalProdutos(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.trocar_tela_callback = trocar_tela_callback
    self.usuario = usuario

    frame = ctk.CTkFrame(self, fg_color="transparent")
    frame.pack(expand=True)

    titulo = ctk.CTkLabel(frame, text="Gerenciar Cardápio", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 20))

    #--- Botão para cadastrar Categoria
    botao_cadastrar_cat = ctk.CTkButton(
      frame,
      text="Cadastrar nova categoria",
      command=self.mostrar_tela_cadastro_cat,
      height=45,
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#a75427",
      hover_color="#a75427",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    
    #--- Botão para listar as categorias cadastradas
    botao_listar_cat = ctk.CTkButton(
      frame,
      text="Categorias cadastradas",
      command=self.mostrar_tela_listar_cat,
      height=45,
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#a75427",
      hover_color="#a75427",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    
    # --- Botão para cadastrar um produto
    botao_cadastrar = ctk.CTkButton(
      frame,
      text="Cadastrar novo produto",
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
      text="Produtos cadastrados",
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

    botao_cadastrar_cat.pack(pady=10, fill="x")
    botao_listar_cat.pack(pady=10, fill="x")
    botao_cadastrar.pack(pady=10, fill="x")
    botao_listar.pack(pady=10, fill="x")
    botao_voltar.pack(pady=10, fill="x")
    
  #--- Função para mostrar a tela de cadastro da categoria
  def mostrar_tela_cadastro_cat(self):
    self.trocar_tela_callback(TelaCadastroCategoria, self.usuario)

  #--- Função para mostrar a tela de listagem das categorias cadastradas
  def mostrar_tela_listar_cat(self):
    self.trocar_tela_callback(TelaListagemCategoria, self.usuario)

  #--- Função para mostrar a tela de cadastro do produto
  def mostrar_tela_cadastro(self):
    self.categorias = listar_categorias()
    
    if self.categorias:
      self.trocar_tela_callback(TelaCadastroProduto, self.usuario)
    else:
      messagebox.showwarning("Atenção", "Primeiramente cadastre uma categoria.")
      self.trocar_tela_callback(TelaCadastroCategoria, self.usuario)
      return


  #--- Função para mostrar a tela de listagem dos produtos cadastrados
  def mostrar_tela_listar(self):
    self.trocar_tela_callback(TelaListagemProduto, self.usuario)

  #--- Função para voltar a tela anterior
  def voltar(self):
    from interface.tela_gerenciamento import TelaGerenciamento
    self.trocar_tela_callback(TelaGerenciamento, self.usuario)