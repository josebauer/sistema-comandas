import customtkinter as ctk
from tkinter import messagebox
from classes.usuario import Usuario
from data.usuarios import cadastrar_usuario_bd

class TelaCadastro(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario=None):
    super().__init__(master)
    self.usuario_logado = usuario
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self)
    self.frame.pack(padx=20, pady=20, fill="both", expand=True)

    titulo = ctk.CTkLabel(self.frame, text="Cadastro de Usuário", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 10))

    self.input_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome completo", height=40)
    self.input_nome.pack(pady=5, fill="x")

    self.input_cpf = ctk.CTkEntry(self.frame, placeholder_text="CPF (somente números)", height=40)
    self.input_cpf.pack(pady=5, fill="x")

    self.input_email = ctk.CTkEntry(self.frame, placeholder_text="Email", height=40)
    self.input_email.pack(pady=5, fill="x")

    self.input_senha = ctk.CTkEntry(self.frame, placeholder_text="Senha", show="*", height=40)
    self.input_senha.pack(pady=5, fill="x")
    
    self.input_repetir_senha = ctk.CTkEntry(self.frame, placeholder_text="Repetir Senha", show="*", height=40)
    self.input_repetir_senha.pack(pady=5, fill="x")

    self.combo_funcao = ctk.CTkOptionMenu(self.frame, values=["Atendente", "Administrador"])
    self.combo_funcao.set("Atendente")
    self.combo_funcao.pack(pady=5, fill="x")

    self.botao_cadastrar = ctk.CTkButton(self.frame, text="Cadastrar", command=self.cadastrar_usuario, height=40)
    self.botao_cadastrar.pack(pady=(15, 5), fill="x")

    self.botao_voltar = ctk.CTkButton(self.frame, text="Voltar", command=self.voltar, height=40)
    self.botao_voltar.pack(fill="x")

  def cadastrar_usuario(self):
    nome = self.input_nome.get().strip()
    cpf = self.input_cpf.get().strip()
    email = self.input_email.get().strip()
    senha = self.input_senha.get().strip()
    repetir_senha = self.input_repetir_senha.get().strip()
    funcao = self.combo_funcao.get()

    if not nome or not cpf or not email or not senha:
      messagebox.showwarning("Erro", "Preencha todos os campos.")
      return

    if senha != repetir_senha:
      messagebox.showwarning("Erro", "As senhas não conferem")
      return

    novo_usuario = Usuario(nome, cpf, email, senha, funcao)

    try:
      cadastrar_usuario_bd(novo_usuario)
      messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
      self.voltar()
    except Exception as e:
      messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)
