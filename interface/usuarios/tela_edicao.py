import customtkinter as ctk
from tkinter import messagebox
from data.usuarios import usuarios

class TelaEdicao(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario_logado = usuario
    self.trocar_tela_callback = trocar_tela_callback
    self.usuario_encontrado = None

    self.frame = ctk.CTkFrame(self)
    self.frame.pack(padx=20, pady=20, fill="both", expand=True)

    self.label_cpf = ctk.CTkLabel(self.frame, text="CPF do usuário:")
    self.label_cpf.pack(pady=(10, 0))
    self.input_cpf_busca = ctk.CTkEntry(self.frame, height=40)
    self.input_cpf_busca.pack(pady=(0, 10))

    self.botao_buscar = ctk.CTkButton(self.frame, text="Buscar", command=self.buscar_usuario, height=35)
    self.botao_buscar.pack(pady=(0, 20))

    self.label_nome = ctk.CTkLabel(self.frame, text="Nome:")
    self.label_nome.pack()
    self.input_nome = ctk.CTkEntry(self.frame, height=40)
    self.input_nome.pack(pady=(0, 10))

    self.label_email = ctk.CTkLabel(self.frame, text="Email:")
    self.label_email.pack()
    self.input_email = ctk.CTkEntry(self.frame, height=40)
    self.input_email.pack(pady=(0, 10))

    self.label_senha = ctk.CTkLabel(self.frame, text="Senha:")
    self.label_senha.pack()
    self.input_senha = ctk.CTkEntry(self.frame, height=40, show="*")
    self.input_senha.pack(pady=(0, 10))

    self.label_funcao = ctk.CTkLabel(self.frame, text="Função:")
    self.label_funcao.pack()
    self.input_funcao = ctk.CTkComboBox(self.frame, values=["Atendente", "Administrador"], height=40)
    self.input_funcao.pack(pady=(0, 20))

    self.botao_salvar = ctk.CTkButton(self.frame, text="Salvar alterações", command=self.salvar_edicao, height=45)
    self.botao_salvar.pack(pady=(0, 10))
    self.botao_salvar.configure(state="disabled")

    self.botao_voltar = ctk.CTkButton(self.frame, text="Voltar", command=self.voltar, height=40)
    self.botao_voltar.pack(pady=(10, 0))

  def buscar_usuario(self):
    cpf_texto = self.input_cpf_busca.get().strip()
    try:
      cpf = int(cpf_texto)
    except ValueError:
      messagebox.showwarning("Erro", "CPF inválido.")
      return

    for usuario in usuarios:
      if usuario.cpf == cpf:
        self.usuario_encontrado = usuario
        self.input_nome.delete(0, 'end')
        self.input_nome.insert(0, usuario.nome)
        self.input_email.delete(0, 'end')
        self.input_email.insert(0, usuario.email)
        self.input_senha.delete(0, 'end')
        self.input_senha.insert(0, usuario.senha)
        self.input_funcao.set(usuario.funcao)
        self.botao_salvar.configure(state="normal")
        return

    messagebox.showinfo("Não encontrado", "Usuário não encontrado.")

  def salvar_edicao(self):
    if not self.usuario_encontrado:
      return

    self.usuario_encontrado.nome = self.input_nome.get().strip()
    self.usuario_encontrado.email = self.input_email.get().strip()
    self.usuario_encontrado.senha = self.input_senha.get().strip()
    self.usuario_encontrado.funcao = self.input_funcao.get()

    messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso.")
    self.botao_salvar.configure(state="disabled")

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)