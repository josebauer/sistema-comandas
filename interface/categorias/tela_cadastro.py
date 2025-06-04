import customtkinter as ctk
from tkinter import messagebox
from classes.categoria import Categoria 
from data.categorias import cadastrar_categoria_db

class TelaCadastroCategoria(ctk.CTkFrame):
    def __init__(self, master, trocar_tela_callback, usuario_logado=None):
        super().__init__(master)
        self.usuario_logado = usuario_logado
        self.trocar_tela_callback = trocar_tela_callback

        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(expand=True)

        titulo = ctk.CTkLabel(self.frame, text="Cadastro de Categoria", font=ctk.CTkFont(size=18, weight="bold"))
        titulo.pack(pady=(0, 20))

        validar_cmd = self.register(self.validar_nome)
        self.input_nome = ctk.CTkEntry(
            self.frame,
            placeholder_text="Nome da categoria",
            height=40,
            width=400,
            validate="key",
            validatecommand=(validar_cmd, "%P")
        )
        self.input_nome.pack(pady=5, padx=10)

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
            command=self.cadastrar_categoria,
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

    def cadastrar_categoria(self):
        nome = self.input_nome.get().strip()

        if not nome:
            messagebox.showwarning("Erro", "Informe o nome da categoria.")
            return

        try:
            categoria = Categoria(nome)
            cadastrar_categoria_db(categoria)
            messagebox.showinfo("Sucesso", "Categoria cadastrada com sucesso!")
            self.voltar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    def voltar(self):
        from interface.produtos.tela_principal import TelaPrincipalProdutos  # ajuste se necessário
        self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario_logado)

    def validar_nome(self, texto):
        return all(c.isalpha() or c.isspace() for c in texto)
