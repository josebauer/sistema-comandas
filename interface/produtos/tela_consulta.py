import customtkinter as ctk
from tkinter import messagebox
from data.produtos import consultar_produto_db
from data.categorias import consultar_categoria_db
from utils.formatacao import formatar_moeda

class TelaConsultaProduto(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario_logado, produto_id_para_ver):
        super().__init__(master)
        self.usuario_logado = usuario_logado
        self.trocar_tela_callback = trocar_tela_callback

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(expand=True, padx=40, pady=40)

        titulo = ctk.CTkLabel(
            container,
            text="Dados do Produto",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=(0, 30))

        self.cartao = ctk.CTkFrame(container, fg_color="#1e1e1e", corner_radius=12, width=400)
        self.cartao.pack(padx=10, pady=10, fill="both", expand=False)

        self.label_nome = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
        self.label_nome.pack(pady=(30, 5), padx=20, anchor="w")

        self.label_valor = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
        self.label_valor.pack(pady=5, padx=20, anchor="w")

        self.label_categoria = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
        self.label_categoria.pack(pady=5, padx=20, anchor="w")

        self.label_descricao = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w", wraplength=360, justify="left")
        self.label_descricao.pack(pady=5, padx=20, anchor="w")

        self.label_disponibilidade = ctk.CTkLabel(self.cartao, text="", font=ctk.CTkFont(size=18), anchor="w")
        self.label_disponibilidade.pack(pady=(5, 30), padx=20, anchor="w")

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

        self.mostrar_produto(produto_id_para_ver)

    def mostrar_produto(self, produto_id):
        produto = consultar_produto_db(produto_id)
        if produto:
            categoria = consultar_categoria_db(produto.id_categoria)
            valor_formatado = formatar_moeda(produto.valor)
            nome_categoria = categoria.nome if categoria else "Categoria não encontrada"

            self.label_nome.configure(text=f"Nome:   {produto.nome}")
            self.label_valor.configure(text=f"Valor:   R$ {valor_formatado}")
            self.label_categoria.configure(text=f"Categoria:   {nome_categoria}")
            self.label_descricao.configure(text=f"Descrição:   {produto.descricao or 'Sem descrição'}")
            disponibilidade = "Disponível" if produto.disponibilidade else "Indisponível"
            self.label_disponibilidade.configure(text=f"Disponibilidade:   {disponibilidade}")
        else:
            messagebox.showinfo("Não encontrado", "Produto não encontrado.")
            self.label_nome.configure(text="")
            self.label_valor.configure(text="")
            self.label_categoria.configure(text="")
            self.label_descricao.configure(text="")
            self.label_disponibilidade.configure(text="")

    def voltar(self):
        from interface.produtos.tela_listagem import TelaListagemProduto
        self.trocar_tela_callback(TelaListagemProduto, self.usuario_logado)