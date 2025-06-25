import customtkinter as ctk
from tkinter import messagebox
from data.pedidos import atualizar_status_pedido

class TelaEdicaoPedido(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado, pedido_encontrado):
    super().__init__(master)
    self.usuario_logado = usuario_logado
    self.pedido_encontrado = pedido_encontrado
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self, fg_color="transparent")
    self.frame.pack(expand=True)

    titulo = ctk.CTkLabel(
      self.frame,
      text="Editar status do pedido",
      font=ctk.CTkFont(size=18, weight="bold")
    )
    titulo.pack(pady=(0, 20))
    
    self.combo_status = ctk.CTkOptionMenu(
      self.frame, values=['Entregue', 'Em preparo', 'Cancelado'],
      fg_color='#366bac', 
      button_color= '#204066',
      button_hover_color= '#366bac',
      height= 40,
      width= 400
    )
    self.combo_status.pack(pady=5, fill="x")
    
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

    self.preencher_campo()

  def preencher_campo(self):
    self.combo_status.set(self.pedido_encontrado._status)

  def salvar_edicao(self):
      status = self.combo_status.get()

      if not status:
        messagebox.showwarning("Erro", "Selecione um status")
        return
      
      self.pedido_encontrado._status = status

      try:
          atualizar_status_pedido(self.pedido_encontrado)
          messagebox.showinfo("Sucesso", "Pedido atualizado com sucesso.")
          self.voltar()
      except Exception as e:
          messagebox.showerror("Erro", f"Erro ao atualizar pedido: {e}")

  def voltar(self):
    from interface.pedidos.tela_listagem import TelaListagemPedidos
    self.trocar_tela_callback(TelaListagemPedidos, self.usuario_logado)