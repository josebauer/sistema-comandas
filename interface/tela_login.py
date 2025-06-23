import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import login_usuario
from interface.tela_gerenciamento import TelaGerenciamento
from interface.tela_atendente import TelaAtendente

class TelaLogin(ctk.CTkFrame):
  def __init__(self, master, trocar_tela):
    super().__init__(master)
    self.trocar_tela = trocar_tela

    # Frame central para centralização vertical e horizontal
    frame_conteudo = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=12, width=500)
    frame_conteudo.pack(expand=True)

    label = ctk.CTkLabel(frame_conteudo, text="Olá, insira suas credenciais abaixo:", font=ctk.CTkFont(size=18, weight="bold"))
    label.pack(pady=30, padx=40)

    self.email_input = ctk.CTkEntry(frame_conteudo, placeholder_text="E-mail", height=40, width=300)
    self.email_input.pack(pady=10)

    self.senha_input = ctk.CTkEntry(frame_conteudo, placeholder_text="Senha", show="*", height=40, width=300)
    self.senha_input.pack(pady=10)

    botao_login = ctk.CTkButton(
      frame_conteudo,
      text="Entrar", 
      command=self.fazer_login,       
      height=32,
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold"),
    )
    botao_login.pack(pady=30)

  def fazer_login(self):
    email = self.email_input.get().strip()
    senha = self.senha_input.get().strip()

    if not email or not senha:
      messagebox.showwarning("Erro", "Preencha todos os campos.")
      return

    usuario = login_usuario(email, senha)

    if usuario:
      if usuario.funcao == "Administrador":
        self.trocar_tela(TelaGerenciamento, usuario)
      else:
        self.trocar_tela(TelaAtendente, usuario)
    else:
      messagebox.showwarning("Erro", "Email ou senha incorretos.")