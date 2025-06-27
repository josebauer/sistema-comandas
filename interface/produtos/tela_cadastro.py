import customtkinter as ctk
from tkinter import messagebox
from classes.produto import Produto
from data.produtos import cadastrar_produto_db
from data.categorias import listar_categorias

class TelaCadastroProduto(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario=None):
        super().__init__(master)
        self.usuario_logado = usuario
        self.trocar_tela_callback = trocar_tela_callback

        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(expand=True)

        titulo = ctk.CTkLabel(self.frame, text="Cadastro de Produto", font=ctk.CTkFont(size=18, weight="bold"))
        titulo.pack(pady=(0, 20))
        
        validar_cmd = self.register(self.validar_nome)

        self.input_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome do Produto", validate="key", validatecommand=(validar_cmd, "%P"), height=40, width=400)
        self.input_nome.pack(pady=5, padx=10)

        self.input_valor = ctk.CTkEntry(
            self.frame, 
            placeholder_text="Valor (Apenas números)", 
            height=40, 
            width=400
        )
        self.input_valor.pack(pady=5, padx=10)
        self.input_valor.bind("<KeyRelease>", self.formatar_valor_dinamicamente)
        
        self.categorias = listar_categorias()
        self.categorias_dict = {cat.nome: cat.id for cat in self.categorias}
        
        self.combo_categoria = ctk.CTkOptionMenu(
            self.frame,
            values=list(self.categorias_dict.keys()),
            fg_color="#366bac",
            button_color="#204066",
            button_hover_color="#366bac",
            height=40,
            width=400
        )
        if self.categorias:
            self.combo_categoria.set("Selecione uma categoria")
        self.combo_categoria.pack(pady=5, padx=10)

        self.input_descricao = ctk.CTkEntry(self.frame, placeholder_text="Descrição", height=40, width=400)
        self.input_descricao.pack(pady=5, padx=10)

        self.combo_disponibilidade = ctk.CTkOptionMenu(
            self.frame,
            values=["Disponível", "Indisponível"],
            fg_color="#366bac",
            button_color="#204066",  
            button_hover_color="#366bac",
            height=40,
            width=400
        )
        self.combo_disponibilidade.set("Disponível")
        self.combo_disponibilidade.pack(pady=5, padx=10)

        botoes_frame = ctk.CTkFrame(self.frame)
        botoes_frame.pack(pady=(15, 0), padx=10, fill="x")

        self.botao_cadastrar = ctk.CTkButton(
            botoes_frame,
            text="Cadastrar",
            fg_color="transparent",
            border_width=2,
            border_color="#238636",
            hover_color="#238636",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.cadastrar_produto,
            height=40
        )
        self.botao_cadastrar.pack(side="left", expand=True, fill="x", padx=(0, 5))

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

    def formatar_valor_dinamicamente(self, event=None):
        texto = self.input_valor.get()
        numeros = ''.join(filter(str.isdigit, texto))

        if not numeros:
            self.input_valor.delete(0, "end")
            return

        valor_float = int(numeros) / 100
        valor_formatado = f"{valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        self.input_valor.delete(0, "end")
        self.input_valor.insert(0, valor_formatado)
    
    def cadastrar_produto(self):
        nome = self.input_nome.get().strip()
        valor = self.input_valor.get().strip()
        categoria_nome = self.combo_categoria.get()
        descricao = self.input_descricao.get().strip()
        disponibilidade = self.combo_disponibilidade.get()

        if not nome or not valor or not categoria_nome or not descricao:
            messagebox.showwarning("Erro", "Preencha todos os campos obrigatórios.")
            return

        try:
            valor = float(valor.replace(',', '.'))
            id_categoria = self.categorias_dict.get(categoria_nome)
            if valor < 0.50:
                messagebox.showwarning("Erro", "O valor não pode ser menor que R$ 0,50.")
                return
        except ValueError:
            messagebox.showwarning("Erro", "Valor deve ser numérico.")
            return

        produto = Produto(
            id=None,
            nome=nome,
            valor=valor,
            id_categoria=id_categoria,
            descricao=descricao,
            disponibilidade=disponibilidade
        )

        try:
            cadastrar_produto_db(produto)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")

    def validar_nome(self, texto):
        return all(c.isalpha() or c.isspace() for c in texto)

    def voltar(self):
        from interface.produtos.tela_principal import TelaPrincipalProdutos
        self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario_logado)

    def limpar_campos(self):
        self.input_nome.delete(0, "end")
        self.input_valor.delete(0, "end")
        self.input_descricao.delete(0, "end")
        self.combo_disponibilidade.set("Disponível")
        if self.categorias:
            self.combo_categoria.set("Selecione uma categoria")
