import customtkinter as ctk
from interface.usuarios.tela_cadastro import TelaCadastro
from interface.usuarios.tela_listagem import TelaListagem
from interface.usuarios.tela_consulta import TelaConsulta
from interface.usuarios.tela_edicao import TelaEdicao

class TelaPrincipalUsuarios(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.trocar_tela_callback = trocar_tela_callback
    self.usuario = usuario

    frame = ctk.CTkFrame(self, fg_color="transparent")
    frame.pack(expand=True)

    titulo = ctk.CTkLabel(frame, text="Gerenciar Usuários", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 20))

    botao_cadastrar = ctk.CTkButton(
      frame, 
      text="Cadastrar novo usuário",
      command=self.mostrar_tela_cadastro, 
      height=45, 
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    botao_listar = ctk.CTkButton(
      frame, 
      text="Usuários cadastrados", 
      command=self.mostrar_tela_listar, 
      height=45, 
      width=400,
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )
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

  def mostrar_tela_cadastro(self):
    self.trocar_tela_callback(TelaCadastro, self.usuario)

  def mostrar_tela_listar(self):
    self.trocar_tela_callback(TelaListagem, self.usuario)
    
  def voltar(self):
    from interface.tela_gerenciamento import TelaGerenciamento
    self.trocar_tela_callback(TelaGerenciamento, self.usuario)