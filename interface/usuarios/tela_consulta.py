import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import usuarios

class TelaConsulta(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario_logado = usuario
    self.trocar_tela_callback = trocar_tela_callback

    frame = ctk.CTkFrame(self)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    titulo = ctk.CTkLabel(frame, text="Consultar Usuário por CPF", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 20))

    self.input_cpf = ctk.CTkEntry(frame, placeholder_text="Digite o CPF", height=40)
    self.input_cpf.pack(pady=(0, 10), fill="x")

    self.botao_consultar = ctk.CTkButton(frame, text="Consultar", command=self.consultar_usuario, height=40)
    self.botao_consultar.pack(pady=(0, 20), fill="x")

    self.resultado = ctk.CTkLabel(frame, text="", justify="left")
    self.resultado.pack()

    self.botao_voltar = ctk.CTkButton(frame, text="Voltar", command=self.voltar, height=40)
    self.botao_voltar.pack(pady=(30, 0), fill="x")

  def consultar_usuario(self):
    cpf_texto = self.input_cpf.get().strip()
    try:
      cpf = int(cpf_texto)
    except ValueError:
      messagebox.showwarning("Erro", "CPF inválido.")
      return

    for usuario in usuarios:
      if usuario.cpf == cpf:
        self.resultado.configure(
          text=f"Nome: {usuario.nome}\nEmail: {usuario.email}\nFunção: {usuario.funcao}"
        )
        return

    messagebox.showinfo("Não encontrado", "Usuário não encontrado.")
    self.resultado.configure(text="")

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)
