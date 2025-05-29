import customtkinter as ctk
from interface.usuarios.tela_principal import TelaPrincipalUsuarios
from interface.produtos.tela_principal import TelaPrincipalProdutos 

class TelaGerenciamento(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario = usuario
    self.trocar_tela_callback = trocar_tela_callback

    layout = ctk.CTkFrame(self, corner_radius=10)
    layout.pack(expand=True, fill="both", padx=20, pady=20)

    label = ctk.CTkLabel(layout, text=f"Bem-vindo, {usuario.nome}!", font=ctk.CTkFont(size=16, weight="bold"))
    label.pack(pady=(10, 20))

    botao_geren_usuarios = ctk.CTkButton(layout, text="Gerenciar usuários", command=self.abrir_tela_usuarios, height=45)
    botao_geren_produtos = ctk.CTkButton(layout, text="Gerenciar produtos", command=self.abrir_tela_produtos, height=45)
    botao_geren_pedidos = ctk.CTkButton(layout, text="Gerenciar pedidos", command=self.abrir_tela_pedidos, height=45)
    botao_sair = ctk.CTkButton(layout, text="Sair", command=self.voltar_login, height=45, fg_color="red", hover_color="#cc0000")

    botao_geren_usuarios.pack(pady=10, fill="x")
    botao_geren_produtos.pack(pady=10, fill="x")
    botao_geren_pedidos.pack(pady=10, fill="x")
    botao_sair.pack(pady=10, fill="x")

  def abrir_tela_usuarios(self):
    self.trocar_tela_callback(TelaPrincipalUsuarios, self.usuario)

  def abrir_tela_produtos(self):
    self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario)
    pass
  def abrir_tela_pedidos(self):
      # Quando tiver a tela de pedidos, siga o mesmo padrão:
      # self.trocar_tela_callback(TelaPedidos, self.usuario)
    pass

  def voltar_login(self):
    from interface.tela_login import TelaLogin
    self.trocar_tela_callback(TelaLogin)