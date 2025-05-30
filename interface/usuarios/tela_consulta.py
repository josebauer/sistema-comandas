import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import consultar_usuario_db

class TelaConsulta(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado, usuario_id_para_ver):
    super().__init__(master)
    self.usuario_logado = usuario_logado
    self.trocar_tela_callback = trocar_tela_callback

    container = ctk.CTkFrame(self, fg_color="transparent")
    container.pack(expand=True, padx=40, pady=40)

    titulo = ctk.CTkLabel(
      container,
      text="Dados do Usuário",
      font=ctk.CTkFont(size=24, weight="bold")
    )
    titulo.pack(pady=(0, 30))

    self.cartao = ctk.CTkFrame(container, fg_color="#1e1e1e", corner_radius=12, width=400)
    self.cartao.pack(padx=10, pady=10, fill="both", expand=False)

    self.label_nome = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_nome.pack(pady=(30, 5), padx=20, anchor="w")

    self.label_cpf = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_cpf.pack(pady=5, padx=20, anchor="w")

    self.label_email = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_email.pack(pady=5, padx=20, anchor="w")

    self.label_funcao = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_funcao.pack(pady=(5, 30), padx=20, anchor="w")

    self.botao_voltar = ctk.CTkButton(
      container,
      text="Voltar",
      fg_color="transparent",
      border_width=2,
      border_color="#63a9ff",
      hover_color="#63a9ff",
      font=ctk.CTkFont(size=14, weight="bold"),
      command=self.voltar,
      height=40,
      width=400
    )
    self.botao_voltar.pack(pady=(30, 0))

    self.mostrar_usuario(usuario_id_para_ver)

  def mostrar_usuario(self, usuario_id):
    usuario = consultar_usuario_db(usuario_id)
    if usuario:
      self.label_nome.configure(text=f"Nome:   {usuario.nome}")
      self.label_cpf.configure(text=f"CPF:   {usuario.cpf}")
      self.label_email.configure(text=f"Email:   {usuario.email}")
      self.label_funcao.configure(text=f"Função:   {usuario.funcao}")
    else:
      messagebox.showinfo("Não encontrado", "Usuário não encontrado.")
      self.label_nome.configure(text="")
      self.label_cpf.configure(text="")
      self.label_email.configure(text="")
      self.label_funcao.configure(text="")

  def voltar(self):
    from interface.usuarios.tela_listagem import TelaListagem
    self.trocar_tela_callback(TelaListagem, self.usuario_logado)
