import customtkinter as ctk
from data.categorias import listar_categorias, excluir_categoria_db
from interface.widgets.item_categoria import ItemCategoria
from interface.categorias.tela_consulta import TelaConsultaCategoria
from interface.categorias.tela_edicao import TelaEdicaoCategoria

class TelaListagemCategoria(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario_logado):
        super().__init__(master)
        self.trocar_tela_callback = trocar_tela_callback
        self.usuario_logado = usuario_logado
        
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(expand=True)

        ctk.CTkLabel(self.frame, text="Categorias Cadastradas", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 20))

        self.container = ctk.CTkScrollableFrame(self.frame, width=500, height=500)
        self.container.pack(expand=True)

        self.carregar_categorias()

        self.botao_voltar = ctk.CTkButton(
            self.frame,
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

    def carregar_categorias(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        categorias = listar_categorias()

        if not categorias:
            ctk.CTkLabel(self.container, text="Nenhuma categoria encontrada.").pack(pady=10)
        else:
            for categoria in categorias:
                item = ItemCategoria(
                    master=self.container,
                    categoria=categoria,
                    ver_callback=self.ver_categoria,
                    editar_callback=self.editar_categoria,
                    excluir_callback=self.excluir_categoria,
                )
                item.pack(fill="x", padx=10, pady=5)

    def ver_categoria(self, categoria):
        self.trocar_tela_callback(TelaConsultaCategoria, self.usuario_logado, categoria.id)

    def editar_categoria(self, categoria):
        self.trocar_tela_callback(TelaEdicaoCategoria, self.usuario_logado, categoria)

    def excluir_categoria(self, categoria):
        excluir_categoria_db(categoria.id)
        self.carregar_categorias()

    def voltar(self):
        from interface.produtos.tela_principal import TelaPrincipalProdutos
        self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario_logado)
