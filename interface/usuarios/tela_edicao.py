import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import atualizar_usuario_db

class TelaEdicao(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario_logado = usuario 
    self.usuario_encontrado = usuario 
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self)
    self.frame.pack(padx=20, pady=20, fill="both", expand=True)

    titulo = ctk.CTkLabel(self.frame, text="Editar dados do usuário", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 10))
    
    # --- Nome
    self.input_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome", height=40)
    self.input_nome.pack(pady=5, fill="x")
    
    # --- Email
    self.input_email = ctk.CTkEntry(self.frame, placeholder_text="E-mail", height=40)
    self.input_email.pack(pady=5, fill="x")

    # --- Senha
    self.input_senha = ctk.CTkEntry(self.frame, placeholder_text="Senha", height=40, show="*")
    self.input_senha.pack(pady=5, fill="x")
    
    self.input_repetir_senha = ctk.CTkEntry(self.frame, placeholder_text="Repetir senha", height=40, show="*")
    self.input_repetir_senha.pack(pady=5, fill="x")

    # --- Função
    self.combo_funcao = ctk.CTkOptionMenu(self.frame, values=["Atendente", "Administrador"])
    self.combo_funcao.pack(pady=5, fill="x")

    # --- Botões
    ctk.CTkButton(self.frame, text="Salvar alterações", command=self.salvar_edicao, height=45).pack(pady=5, fill="x")
    ctk.CTkButton(self.frame, text="Voltar", command=self.voltar, height=40).pack(pady=5, fill="x")

    self.preencher_campos()

  def preencher_campos(self):
    self.input_nome.insert(0, self.usuario_encontrado.nome)
    self.input_email.insert(0, self.usuario_encontrado.email)
    self.input_senha.insert(0, self.usuario_encontrado.senha)
    self.combo_funcao.set(self.usuario_encontrado.funcao)

  def salvar_edicao(self):
    self.usuario_encontrado.nome = self.input_nome.get().strip()
    self.usuario_encontrado.email = self.input_email.get().strip()
    self.usuario_encontrado.senha = self.input_senha.get().strip()
    self.usuario_encontrado.repetir_senha = self.input_repetir_senha.get().strip()
    self.usuario_encontrado.funcao = self.combo_funcao.get()
    
    nome = self.usuario_encontrado.nome
    email = self.usuario_encontrado.email
    senha = self.usuario_encontrado.senha
    repetir_senha = self.usuario_encontrado.repetir_senha

    if not nome or not email or not senha or not repetir_senha:
      messagebox.showwarning("Erro", "Preencha todos os campos.")
      return
    
    if senha != repetir_senha:
      messagebox.showwarning("Erro", "As senhas não conferem")
      return
    
    atualizar_usuario_db(self.usuario_encontrado)

    messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso.")
    self.voltar()

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)