import customtkinter as ctk
from tkinter import messagebox
from classes.usuario import Usuario
from data.usuarios import cadastrar_usuario_db

class TelaCadastro(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario=None):
    super().__init__(master)
    self.usuario_logado = usuario
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self, fg_color="transparent")
    self.frame.pack(expand=True)

    titulo = ctk.CTkLabel(self.frame, text="Cadastro de Usuário", font=ctk.CTkFont(size=18, weight="bold"))
    titulo.pack(pady=(0, 20))

    validar_cmd = self.register(self.validar_nome)
    self.input_nome = ctk.CTkEntry(
      self.frame,
      placeholder_text="Nome completo",
      height=40,
      width=400,
      validate="key",
      validatecommand=(validar_cmd, "%P")
    )
    self.input_nome.pack(pady=5, padx=10)

    self.input_cpf = ctk.CTkEntry(self.frame, placeholder_text="CPF (Apenas números)", height=40, width=400)
    self.input_cpf.pack(pady=5, padx=10)
    self.input_cpf.bind("<KeyRelease>", self.formatar_cpf)

    self.input_email = ctk.CTkEntry(self.frame, placeholder_text="Email", height=40, width=400)
    self.input_email.pack(pady=5, padx=10)

    self.input_senha = ctk.CTkEntry(self.frame, placeholder_text="Senha", show="*", height=40, width=400)
    self.input_senha.pack(pady=5, padx=10)
    
    self.input_repetir_senha = ctk.CTkEntry(self.frame, placeholder_text="Repetir Senha", show="*", height=40, width=400)
    self.input_repetir_senha.pack(pady=5, padx=10)

    self.combo_funcao = ctk.CTkOptionMenu(self.frame, values=["Atendente", "Administrador"], fg_color="#366bac", button_color="#204066", button_hover_color="#366bac", height=40, width=400)
    self.combo_funcao.set("Atendente")
    self.combo_funcao.pack(pady=5, padx=10)

    botoes_frame = ctk.CTkFrame(self.frame)
    botoes_frame.pack(pady=(15, 0), padx=10, fill="x")

    self.botao_cadastrar = ctk.CTkButton(
      botoes_frame,
      text="Cadastrar",
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold"),
      command=self.cadastrar_usuario,
      height=40
    )
    self.botao_cadastrar.pack(side="left", expand=True, fill="x", padx=(0, 5))

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

  def cadastrar_usuario(self):
    nome = self.input_nome.get().strip()
    cpf = self.input_cpf.get().strip()
    email = self.input_email.get().strip()
    senha = self.input_senha.get().strip()
    repetir_senha = self.input_repetir_senha.get().strip()
    funcao = self.combo_funcao.get()

    if not nome or not cpf or not email or not senha or not repetir_senha:
      messagebox.showwarning("Erro", "Preencha todos os campos.")
      return
    
    if senha != repetir_senha:
      messagebox.showwarning("Erro", "As senhas não conferem")
      return

    novo_usuario = Usuario(nome, cpf, email, senha, funcao)

    try:
      cadastrar_usuario_db(novo_usuario)
      messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
      self.voltar()
    except Exception as e:
      messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)

  def validar_nome(self, texto):
    return all(c.isalpha() or c.isspace() for c in texto)
  
  def formatar_cpf(self, event=None):
    texto = self.input_cpf.get()
    numeros = ''.join(filter(str.isdigit, texto))

    formatado = ""
    if len(numeros) > 0:
        formatado += numeros[:3]
    if len(numeros) >= 4:
        formatado += "." + numeros[3:6]
    if len(numeros) >= 7:
        formatado += "." + numeros[6:9]
    if len(numeros) >= 10:
        formatado += "-" + numeros[9:11]

    self.input_cpf.delete(0, "end")
    self.input_cpf.insert(0, formatado)