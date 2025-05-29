import customtkinter as ctk
from data.usuarios import usuarios

class TelaListagem(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario = usuario
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self)
    self.frame.pack(padx=20, pady=20, fill="both", expand=True)

    self.titulo = ctk.CTkLabel(self.frame, text="Usuários Cadastrados", font=ctk.CTkFont(size=18, weight="bold"))
    self.titulo.pack(pady=(0, 10))

    self.lista = ctk.CTkTextbox(self.frame, height=200)
    self.lista.pack(fill="both", expand=True)
    self.lista.configure(state="disabled")

    self.btn_voltar = ctk.CTkButton(self.frame, text="Voltar", command=self.voltar, height=40)
    self.btn_voltar.pack(pady=(20, 0))

    self.carregar_usuarios()

  def carregar_usuarios(self):
    self.lista.configure(state="normal")
    self.lista.delete("1.0", "end")

    if not usuarios:
      self.lista.insert("end", "Nenhum usuário cadastrado.\n")
    else:
      for usuario in usuarios:
        self.lista.insert("end", f"{usuario.nome} - {usuario.funcao}\n")

    self.lista.configure(state="disabled")

  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario)