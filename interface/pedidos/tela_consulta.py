import customtkinter as ctk
from tkinter import messagebox
from data.pedidos import consultar_pedido
from utils.formatacao import formatar_moeda

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
    
    cartao_container = ctk.CTkFrame(container, fg_color="transparent", width=500, height=600)
    cartao_container.pack(pady=10)
    cartao_container.pack_propagate(False)

    self.cartao = ctk.CTkScrollableFrame(cartao_container, fg_color="#1e1e1e", corner_radius=12)
    self.cartao.pack(fill="both", expand=True, padx=20) 

    self.label_id = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_id.pack(pady=(30, 0), padx=30, anchor="w")
    
    self.label_data_hora = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=16, slant='italic'), anchor="w")
    self.label_data_hora.pack(pady=(10, 0), padx=30, anchor="w")
    
    self.label_usuario = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=16), anchor="w")
    self.label_usuario.pack(pady=(10, 0), padx=30, anchor="w")
    
    self.label_status = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18, weight="bold"), anchor="w", wraplength=360, justify="left")
    self.label_status.pack(pady=5, padx=30, anchor="w")

    self.divisor = ctk.CTkFrame(self.cartao, height=2, fg_color="#444444")
    self.divisor.pack(fill="x", pady=10, padx=30)
    
    self.label_itens_pedido = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_itens_pedido.pack(pady=5, padx=30, anchor="w")
    
    self.label_itens = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_itens.pack(pady=5, padx=30, anchor="w")
    
    self.label_valor_total = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18, weight="bold"), anchor="w")
    self.label_valor_total.pack(pady=10, padx=30, anchor="w")
    
    self.divisor = ctk.CTkFrame(self.cartao, height=2, fg_color="#444444")
    self.divisor.pack(fill="x", pady=10, padx=30)

    self.label_metodo_pag = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
    self.label_metodo_pag.pack(pady=(0, 30), padx=30, anchor="w")
    
    botoes_frame = ctk.CTkFrame(container)
    botoes_frame.pack(pady=(15, 0), padx=10, fill="x")
    
    self.botao_recibo = ctk.CTkButton(
      botoes_frame,
      text="Emitir recibo",
      fg_color="transparent",
      border_width=2,
      border_color="#238636",
      hover_color="#238636",
      font=ctk.CTkFont(size=14, weight="bold"),
      command=self.emitir_recibo,
      height=40
    )
    self.botao_recibo.pack(side="left", expand=True, fill="x", padx=(0, 5))

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

    self.mostrar_pedido(pedido_id_para_ver)

  def mostrar_pedido(self, pedido_id):
      pedido = consultar_pedido(pedido_id)
      data_formatada = pedido._data_hora.strftime("Data: %d/%m/%Y    Hora: %H:%M")
      
      if pedido:   
        self.label_id.configure(text=f"Pedido n°:   {pedido._id}")
        self.label_data_hora.configure(text=f"{data_formatada}")
        self.label_usuario.configure(text=f"Atendente: {pedido.nome_usuario}")
        self.label_status.configure(text=f"Status:   {pedido._status}")
        
        itens_texto = ""
        for item in pedido.itens:
          obs = f"\n{'Obs: ' + item._observacoes}"
      
          valor_valor_unit_formatado = formatar_moeda(item._valor_unit)
          itens_texto += f"\n- {item._quantidade}x {item._nome} R$ {valor_valor_unit_formatado} {obs if item._observacoes else ''}\n"
          
        self.label_itens_pedido.configure(text=f"Itens do pedido:")
        self.label_itens.configure(text=f"{itens_texto}")
        
        valor_valor_total_formatado = formatar_moeda(pedido._valor_total)
        
        self.label_valor_total.configure(text=f"Valor Total:   R$ {valor_valor_total_formatado}")
        
        self.label_metodo_pag.configure(text=f"Método de pagamento:   {pedido.nome_metodo_pagamento}")
      else:
          messagebox.showinfo("Não encontrado", "pedido não encontrado.")
          self.label_id.configure(text="")
          self.label_valor_total.configure(text="")
          self.label_status.configure(text="")
          self.label_itens.configure(text="")
          self.label_metodo_pag.configure(text="")
          self.label_usuario.configure(text="")
    
  def emitir_recibo(self):
    messagebox.showinfo("Recibo", "Emitindo recibo...")
    
    
  def voltar(self):
      from interface.pedidos.tela_listagem import TelaListagemPedidos
      self.trocar_tela_callback(TelaListagemPedidos, self.usuario_logado)