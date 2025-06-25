import customtkinter as ctk
from tkinter import messagebox
from data.pedidos import consultar_pedido

class TelaConsultaPedido(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado, pedido_id_para_ver):
    super().__init__(master)
    self.usuario_logado = usuario_logado
    self.trocar_tela_callback = trocar_tela_callback

    container = ctk.CTkFrame(self, fg_color="transparent")
    container.pack(expand=True, padx=40, pady=40)

    titulo = ctk.CTkLabel(
        container,
        text="Dados do Pedido",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    titulo.pack(pady=(0, 30))

    self.cartao = ctk.CTkFrame(container, fg_color="#1e1e1e", corner_radius=12, width=400)
    self.cartao.pack(padx=10, pady=10, fill="both", expand=False)

    self.label_id = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_id.pack(pady=5, padx=20, anchor="w")
    
    self.label_valor_total = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_valor_total.pack(pady=5, padx=20, anchor="w")

    self.label_status = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w", wraplength=360, justify="left")
    self.label_status.pack(pady=5, padx=20, anchor="w")

    self.label_itens = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_itens.pack(pady=5, padx=20, anchor="w")

    self.label_metodo_pag = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_metodo_pag.pack(pady=(5, 30), padx=20, anchor="w")
    
    self.label_usuario = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_usuario.pack(pady=(5, 30), padx=20, anchor="w")

    self.botao_voltar = ctk.CTkButton(
        container,
        text="Voltar",
        fg_color="transparent",
        border_width=2,
        border_color="#63a9ff",
        hover_color="#63a9ff",
        font=ctk.CTkFont(size=14, weight="bold"),
        command=self.voltar,
        height=40,
        width=400
    )
    self.botao_voltar.pack(pady=(30, 0))

    self.mostrar_pedido(pedido_id_para_ver)

  def mostrar_pedido(self, pedido_id):
      pedido = consultar_pedido(pedido_id)
      if pedido:   
        self.label_id.configure(text=f"Pedido n°: {pedido._id}")
        self.label_valor_total.configure(text=f"Valor:   R$ {pedido._valor_total:.2f}")
        self.label_status.configure(text=f"Status:   {pedido._status}")
        
        itens_texto = ""
        for item in pedido.itens:
          itens_texto += f"- {item._nome} (Qtd: {item._quantidade}, R${item._valor_unit:.2f})\n"
        self.label_itens.configure(text=f"Itens Pedido:\n{itens_texto}")
            
        self.label_metodo_pag.configure(text=f"Método de pagamento:   {pedido.nome_metodo_pagamento}")
        self.label_usuario.configure(text=f"Atendente responsável: {pedido.nome_usuario}")
      else:
          messagebox.showinfo("Não encontrado", "pedido não encontrado.")
          self.label_id.configure(text="")
          self.label_valor_total.configure(text="")
          self.label_status.configure(text="")
          self.label_itens.configure(text="")
          self.label_metodo_pag.configure(text="")
          self.label_usuario.configure(text="")

  def voltar(self):
      from interface.pedidos.tela_listagem import TelaListagemPedidos
      self.trocar_tela_callback(TelaListagemPedidos, self.usuario_logado)