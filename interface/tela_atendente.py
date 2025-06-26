import customtkinter as ctk
from interface.pedidos.tela_cadastro import TelaCadastroPedido
from interface.pedidos.tela_listagem import TelaListagemPedidos

class TelaAtendente(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario):
    super().__init__(master)
    self.usuario = usuario
    self.trocar_tela_callback = trocar_tela_callback

    layout = ctk.CTkFrame(self, fg_color="transparent")
    layout.pack(expand=True)

    label = ctk.CTkLabel(layout, text=f"Bem-vindo, {usuario.nome}!", font=ctk.CTkFont(size=18, weight="bold"))
    label.pack(pady=(0, 20))

    botao_realizar_pedido = ctk.CTkButton(
      layout, 
      text="Realizar novo pedido", 
      command=self.abrir_tela_novo_pedido, 
      height=45, 
      width=400, 
      fg_color="transparent",
      border_width=2,
      border_color="#63a9ff",
      hover_color="#63a9ff",
      font=ctk.CTkFont(size=14, weight="bold")
    )
    
    botao_lista_pedidos = ctk.CTkButton(
      layout, 
      text="Pedidos Realizados", 
      command=self.abrir_tela_pedidos, 
      height=45, 
      width=400, 
      fg_color="transparent",
      border_width=2,
      border_color="#63a9ff",
      hover_color="#63a9ff",
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
    
    botao_realizar_pedido.pack(pady=10)
    botao_lista_pedidos.pack(pady=10)
    botao_sair.pack(pady=10)
    
  def abrir_tela_novo_pedido(self):
    self.trocar_tela_callback(TelaCadastroPedido, self.usuario)
  
  def abrir_tela_pedidos(self):
    self.trocar_tela_callback(TelaListagemPedidos, self.usuario)
  
  def voltar_login(self):
    from interface.tela_login import TelaLogin
    self.trocar_tela_callback(TelaLogin)