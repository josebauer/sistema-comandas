import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import consultar_usuario_db

class TelaConsulta(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado, usuario_id_para_ver):
    super().__init__(master)
    self.usuario_logado = usuario_logado
    self.trocar_tela_callback = trocar_tela_callback

    frame = ctk.CTkFrame(self)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    self.resultado = ctk.CTkLabel(frame, text="", justify="left")
    self.resultado.pack(pady=10)

    self.botao_voltar = ctk.CTkButton(frame, text="Voltar", command=self.voltar, height=40)
    self.botao_voltar.pack(pady=(30, 0), fill="x")

    self.mostrar_usuario(usuario_id_para_ver)

  def mostrar_usuario(self, usuario_id):
    usuario = consultar_usuario_db(usuario_id)
    if usuario:
      self.resultado.configure(
          text=f"Nome: {usuario.nome}\nCPF: {usuario.cpf}\nEmail: {usuario.email}\nFunção: {usuario.funcao}"
      )
    else:
      messagebox.showinfo("Não encontrado", "Usuário não encontrado.")
      self.resultado.configure(text="")

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)
