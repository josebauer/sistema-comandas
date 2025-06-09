import customtkinter as ctk
from interface.usuarios.tela_principal import TelaPrincipalUsuarios
from interface.produtos.tela_principal import TelaPrincipalProdutos 
from interface.pedidos.tela_principal import TelaPrincipalPedidos

class TelaGerenciamento(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario = usuario
    self.trocar_tela_callback = trocar_tela_callback

    
    layout = ctk.CTkFrame(self, fg_color="transparent")
    layout.pack(expand=True)

    label = ctk.CTkLabel(layout, text=f"Bem-vindo, {usuario.nome}!", font=ctk.CTkFont(size=18, weight="bold"))
    label.pack(pady=(0, 20))

    botao_geren_usuarios = ctk.CTkButton(
      layout, 
      text="Gerenciar usuários", 
      command=self.abrir_tela_usuarios, 
      height=45, 
      width=400, 
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    botao_geren_produtos = ctk.CTkButton(
      layout, 
      text="Gerenciar cardápio", 
      command=self.abrir_tela_produtos, 
      height=45, 
      width=400, 
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    botao_geren_pedidos = ctk.CTkButton(
      layout, 
      text="Gerenciar pedidos", 
      command=self.abrir_tela_pedidos, 
      height=45, 
      width=400, 
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    botao_sair = ctk.CTkButton(
      layout, 
      text="Sair", 
      command=self.voltar_login, 
      height=45, 
      width=400, 
      fg_color="transparent",
      border_width=2,
      border_color="#cc0000",
      hover_color="#cc0000", 
      font=ctk.CTkFont(size=14, weight="bold"),  
    )

    botao_geren_usuarios.pack(pady=10)

    botao_geren_produtos.pack(pady=10)
    botao_geren_pedidos.pack(pady=10)
    botao_sair.pack(pady=10)

  def abrir_tela_usuarios(self):
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario)

  def abrir_tela_produtos(self):
    self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario)
    pass
  def abrir_tela_pedidos(self):
    self.trocar_tela_callback(TelaPrincipalPedidos, self.usuario)
    pass

  def voltar_login(self):
    from interface.tela_login import TelaLogin
    self.trocar_tela_callback(TelaLogin)