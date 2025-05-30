import customtkinter as ctk
from data.usuarios import listar_usuarios
from interface.widgets.item_usuario import ItemUsuario
from interface.usuarios.tela_consulta import TelaConsulta
from interface.usuarios.tela_edicao import TelaEdicao

class TelaListagem(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado):
    super().__init__(master)
    self.trocar_tela_callback = trocar_tela_callback
    self.usuario_logado = usuario_logado
    
    ctk.CTkLabel(self, text="Usuários Cadastrados", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(40, 0))

    self.container = ctk.CTkScrollableFrame(self, width=550, height=350)
    self.container.pack(expand=True)

    self.carregar_usuarios()

    self.botao_voltar = ctk.CTkButton(
        self,
        text="Voltar",
        fg_color="transparent",
        border_width=2,
        border_color="#63a9ff",
        hover_color="#63a9ff",
        font=ctk.CTkFont(size=14, weight="bold"),
        command=self.voltar,
        height=40,
        width=250
      )
    self.botao_voltar.pack(pady=(0, 40), side="left", expand=True)


  def carregar_usuarios(self):
    for widget in self.container.winfo_children():
      widget.destroy()

    usuarios = listar_usuarios()

    if not usuarios:
      ctk.CTkLabel(self.container, text="Nenhum usuário encontrado.").pack(pady=10)
    else:
      for usuario in usuarios:
        item = ItemUsuario(
          master=self.container,
          usuario=usuario,
          ver_callback=self.ver_usuario,
          editar_callback=self.editar_usuario,
          excluir_callback=self.excluir_usuario,
        )
        item.pack(fill="x", padx=10, pady=5)

  def ver_usuario(self, usuario):
    self.trocar_tela_callback(TelaConsulta, self.usuario_logado, usuario.id)
    
  def editar_usuario(self, usuario):
    self.trocar_tela_callback(TelaEdicao, usuario)

  def excluir_usuario(self, usuario):
    from data.usuarios import excluir_usuario_db
    excluir_usuario_db(usuario.id)
    self.carregar_usuarios() 
  
  def voltar(self):
    from interface.usuarios.tela_principal import TelaPrincipalUsuarios
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario_logado)