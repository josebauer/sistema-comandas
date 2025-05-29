import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import login_usuario
from interface.tela_gerenciamento import TelaGerenciamento

class TelaLogin(ctk.CTkFrame):
  def __init__(self, master, trocar_tela):
    super().__init__(master)
    self.trocar_tela = trocar_tela

    label = ctk.CTkLabel(self, text="Bem vindo! Insira suas credenciais abaixo:", font=('system-ui', 18))
    label.pack(pady=20)

    self.email_input = ctk.CTkEntry(self, placeholder_text="Email")
    self.email_input.pack(pady=10, fill="x", padx=100)

    self.senha_input = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
    self.senha_input.pack(pady=10, fill="x", padx=100)

    botao_login = ctk.CTkButton(self, text="Entrar", command=self.fazer_login)
    botao_login.pack(pady=20)

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
        messagebox.showinfo("Login", f"Bem-vindo, {usuario.nome}!")
    else:
      messagebox.showwarning("Erro", "Email ou senha incorretos.")