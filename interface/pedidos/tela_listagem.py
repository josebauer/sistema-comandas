import customtkinter as ctk
from data.pedidos import listar_pedidos_por_status
from data.pedidos import listar_pedidos
from interface.widgets.item_pedido_lista import ItemPedidoLista
from interface.pedidos.tela_consulta import TelaConsultaPedido
from interface.pedidos.tela_edicao import TelaEdicaoPedido

class TelaListagemPedidos(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario_logado):
        super().__init__(master)
        self.trocar_tela_callback = trocar_tela_callback
        self.usuario_logado = usuario_logado

        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(expand=True)

        ctk.CTkLabel(
            self.frame, text="Pedidos Realizados", 
            
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(0, 20))
        
        botoes_topo_frame = ctk.CTkFrame(self.frame)
        botoes_topo_frame.pack(pady=10, fill="x")
                
        ctk.CTkButton(
            botoes_topo_frame, text="Pedidos pendentes",
            command=lambda: self.carregar_pedidos_por_status('Em preparo'),
            fg_color="transparent", border_width=2,
            border_color="#a38626", hover_color="#a38626",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            width=250
        ).pack(pady=(0, 10), side="left", expand=True)
        
        ctk.CTkButton(
            botoes_topo_frame, text="Pedidos entregues",
            command=lambda: self.carregar_pedidos_por_status('Entregue'),
            fg_color="transparent", border_width=2,
            border_color="#238636", hover_color="#238636",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            width=250
        ).pack(pady=(0, 10), side="left", expand=True)
                
        botoes_topo_frame_2 = ctk.CTkFrame(self.frame)
        botoes_topo_frame_2.pack(pady=10, fill="x")
        
        ctk.CTkButton(
            botoes_topo_frame_2, text="Pedidos cancelados",
            command=lambda: self.carregar_pedidos_por_status('Cancelado'),
            fg_color="transparent", border_width=2,
            border_color="#cc0000", hover_color="#cc0000",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            width=250
        ).pack(pady=(0, 20), side="left", expand=True)
        
        ctk.CTkButton(
            botoes_topo_frame_2, text="Todos os pedidos",
            command=lambda: self.carregar_pedidos(),
            fg_color="transparent", border_width=2,
            border_color="#63a9ff", hover_color="#63a9ff",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            width=250
        ).pack(pady=(0, 20), side="left", expand=True)
        

        self.scroll_frame = ctk.CTkScrollableFrame(self.frame, width=600, height=600)
        self.scroll_frame.pack()

        botoes_frame = ctk.CTkFrame(self.frame)
        botoes_frame.pack(pady=10, fill="x")

        ctk.CTkButton(
            botoes_frame, text="Voltar",
            command=self.voltar,
            fg_color="transparent", border_width=2,
            border_color="#63a9ff", hover_color="#63a9ff",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            width=250
        ).pack(pady=(0, 40), side="left", expand=True)

        self.carregar_pedidos()

    def carregar_pedidos_por_status(self, status):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
            
        pedidos = listar_pedidos_por_status(status)
    
        if not pedidos:
            ctk.CTkLabel(self.scroll_frame, text="Nenhum pedido encontrado.").pack(pady=10)
            return

        for pedido in pedidos:
            item = ItemPedidoLista(
                master=self.scroll_frame,
                pedido=pedido,
                ver_callback=self.ver_pedido,
                editar_callback=self.editar_status_pedido
            )
            item.pack(padx=5, pady=5, fill="x")

    def carregar_pedidos(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        pedidos = listar_pedidos()

        if not pedidos:
            ctk.CTkLabel(self.scroll_frame, text="Nenhum pedido encontrado.").pack(pady=10)
            return

        for pedido in pedidos:
            item = ItemPedidoLista(
                master=self.scroll_frame,
                pedido=pedido,
                ver_callback=self.ver_pedido,
                editar_callback=self.editar_status_pedido
            )
            item.pack(padx=5, pady=5, fill="x")

    def ver_pedido(self, pedido):
        self.trocar_tela_callback(TelaConsultaPedido, self.usuario_logado, pedido._id)

    def editar_status_pedido(self, pedido):
        self.trocar_tela_callback(TelaEdicaoPedido, self.usuario_logado, pedido)
        
    def voltar(self):
        if self.usuario_logado.funcao == 'Administrador':
            from interface.tela_gerenciamento import TelaGerenciamento
            self.trocar_tela_callback(TelaGerenciamento, self.usuario_logado)
        else:
            from interface.tela_atendente import TelaAtendente
            self.trocar_tela_callback(TelaAtendente, self.usuario_logado)