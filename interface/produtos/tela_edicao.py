import customtkinter as ctk
from tkinter import messagebox
from data.categorias import listar_categorias
from data.produtos import atualizar_produto_db
from utils.formatacao import formatar_moeda

class TelaEdicaoProduto(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario_logado, produto_encontrado):
        super().__init__(master)
        self.usuario_logado = usuario_logado
        self.produto_encontrado = produto_encontrado
        self.trocar_tela_callback = trocar_tela_callback

        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(expand=True)

        titulo = ctk.CTkLabel(
            self.frame,
            text="Editar dados do produto",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        titulo.pack(pady=(0, 20))

        validar_cmd = self.register(self.validar_nome)
        
        self.input_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome do Produto", validate="key", validatecommand=(validar_cmd, "%P"), height=40, width=400)
        self.input_nome.pack(pady=5, fill="x")

        self.input_valor = ctk.CTkEntry(
            self.frame, 
            placeholder_text="Valor (Apenas números)", 
            height=40, 
            width=400
        )
        self.input_valor.pack(pady=5, fill="x")
        self.input_valor.bind("<KeyRelease>", self.formatar_valor_dinamicamente)

        # Carregar categorias
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
        self.combo_categoria.pack(pady=5, fill="x")

        self.input_descricao = ctk.CTkEntry(self.frame, placeholder_text="Descrição", height=40, width=400)
        self.input_descricao.pack(pady=5, fill="x")

        self.combo_disponibilidade = ctk.CTkOptionMenu(
            self.frame,
            values=["Disponível", "Indisponível"],
            fg_color="#366bac",
            button_color="#204066",
            button_hover_color="#366bac",
            height=40,
            width=400
        )
        self.combo_disponibilidade.pack(pady=5, fill="x")

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

        self.preencher_campos()
    
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
        
    def validar_nome(self, texto):
        return all(c.isalpha() or c.isspace() for c in texto)

    def preencher_campos(self):
        valor_formatado = formatar_moeda(self.produto_encontrado.valor)
        self.input_nome.insert(0, self.produto_encontrado.nome)
        self.input_valor.insert(0, str(valor_formatado))

        nome_categoria = next(
            (nome for nome, id_ in self.categorias_dict.items() if id_ == self.produto_encontrado.id_categoria),
            None
        )
        if nome_categoria:
            self.combo_categoria.set(nome_categoria)

        self.input_descricao.insert(0, self.produto_encontrado.descricao or "")
        self.combo_disponibilidade.set(self.produto_encontrado.disponibilidade)

    def salvar_edicao(self):
        nome = self.input_nome.get().strip()
        valor = self.input_valor.get().strip()
        nome_categoria = self.combo_categoria.get().strip()
        descricao = self.input_descricao.get().strip()
        disponibilidade = self.combo_disponibilidade.get()

        if not nome or not valor or not nome_categoria or not descricao:
            messagebox.showwarning("Erro", "Preencha todos os campos.")
            return

        try:
            valor = float(valor.replace(',', '.'))
            if valor < 0.50:
                messagebox.showwarning("Erro", "O valor não pode ser menor ou igual a zero.")
                return
        except ValueError:
            messagebox.showwarning("Erro", "O valor deve ser um número válido.")
            return

        id_categoria = self.categorias_dict.get(nome_categoria)
        if id_categoria is None:
            messagebox.showerror("Erro", "Categoria inválida.")
            return

        self.produto_encontrado.nome = nome
        self.produto_encontrado.valor = valor
        self.produto_encontrado.id_categoria = id_categoria
        self.produto_encontrado.descricao = descricao
        self.produto_encontrado.disponibilidade = disponibilidade

        try:
            atualizar_produto_db(self.produto_encontrado)
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")
            self.voltar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")

    def voltar(self):
        from interface.produtos.tela_principal import TelaPrincipalProdutos
        self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario_logado)