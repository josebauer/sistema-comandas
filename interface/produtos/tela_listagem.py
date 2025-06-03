import customtkinter as ctk
from data.produtos import listar_produtos, excluir_produto_db
from interface.widgets.item_produto import ItemProduto
from interface.produtos.tela_consulta import TelaConsultaProduto
from interface.produtos.tela_edicao import TelaEdicaoProduto

class TelaListagemProduto(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario_logado):
        super().__init__(master)
        self.trocar_tela_callback = trocar_tela_callback
        self.usuario_logado = usuario_logado

        ctk.CTkLabel(self, text="Produtos Cadastrados", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(40, 0))

        self.container = ctk.CTkScrollableFrame(self, width=550, height=350)
        self.container.pack(expand=True)

        self.carregar_produtos()

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

    def carregar_produtos(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        produtos = listar_produtos()

        if not produtos:
            ctk.CTkLabel(self.container, text="Nenhum produto encontrado.").pack(pady=10)
        else:
            for produto in produtos:
                item = ItemProduto(
                    master=self.container,
                    produto=produto,
                    ver_callback=self.ver_produto,
                    editar_callback=self.editar_produto,
                    excluir_callback=self.excluir_produto
                )
                item.pack(fill="x", padx=10, pady=5)

    def ver_produto(self, produto):
        self.trocar_tela_callback(TelaConsultaProduto, self.usuario_logado, produto.id)

    def editar_produto(self, produto):
        self.trocar_tela_callback(TelaEdicaoProduto, self.usuario_logado, produto)

    def excluir_produto(self, produto):
        excluir_produto_db(produto.id)
        self.carregar_produtos()

    def voltar(self):
        from interface.produtos.tela_principal import TelaPrincipalProdutos
        self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario_logado)
