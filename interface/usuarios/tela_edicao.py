import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import atualizar_usuario_db

class TelaEdicao(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario_logado = usuario 
    self.usuario_encontrado = usuario 
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self, fg_color="transparent")
    self.frame.pack(expand=True)

    titulo = ctk.CTkLabel(self.frame, text="Editar dados do usuário", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 20))
    
    # --- Nome
    self.input_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome", height=40, width=400)
    self.input_nome.pack(pady=5, fill="x")
    
    # --- Email
    self.input_email = ctk.CTkEntry(self.frame, placeholder_text="E-mail", height=40, width=400)
    self.input_email.pack(pady=5, fill="x")

    # --- Senha
    self.input_senha = ctk.CTkEntry(self.frame, placeholder_text="Senha", height=40, width=400, show="*")
    self.input_senha.pack(pady=5, fill="x")
    
    self.input_repetir_senha = ctk.CTkEntry(self.frame, placeholder_text="Repetir senha", height=40, width=400, show="*")
    self.input_repetir_senha.pack(pady=5, fill="x")

    # --- Função
    self.combo_funcao = ctk.CTkOptionMenu(self.frame, values=["Atendente", "Administrador"], height=40, width=400)
    self.combo_funcao.pack(pady=5, fill="x")

    # --- Botões
    botoes_frame = ctk.CTkFrame(self.frame)
    botoes_frame.pack(pady=(15, 0), padx=10, fill="x")
    
    self.botao_salvar = ctk.CTkButton(
      botoes_frame,
      text="Salvar alterações",
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold"),
      command=self.salvar_edicao,
      height=40
    )
    self.botao_salvar.pack(side="left", expand=True, fill="x", padx=(0, 5))

    self.botao_voltar = ctk.CTkButton(
      botoes_frame,
      text="Voltar",
      fg_color="transparent",
      border_width=2,
      border_color="#63a9ff",
      hover_color="#63a9ff",
      font=ctk.CTkFont(size=14, weight="bold"),
      command=self.voltar,
      height=40
    )
    self.botao_voltar.pack(side="left", expand=True, fill="x", padx=(5, 0))

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