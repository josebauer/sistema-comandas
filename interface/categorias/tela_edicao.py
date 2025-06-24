import customtkinter as ctk
from tkinter import messagebox
from data.categorias import atualizar_categoria_db

class TelaEdicaoCategoria(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado, categoria_encontrada):
    super().__init__(master)
    self.usuario_logado = usuario_logado
    self.categoria_encontrada = categoria_encontrada
    self.trocar_tela_callback = trocar_tela_callback

    self.frame = ctk.CTkFrame(self, fg_color="transparent")
    self.frame.pack(expand=True)

    titulo = ctk.CTkLabel(
      self.frame,
      text="Editar nome da categoria",
      font=ctk.CTkFont(size=18, weight="bold")
    )
    titulo.pack(pady=(0, 20))
    
    validar_cmd = self.register(self.validar_nome)

    self.input_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome da categoria",       validate="key", validatecommand=(validar_cmd, "%P"), height=40, width=400)
    self.input_nome.pack(pady=5, fill="x")
    
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

  def validar_nome(self, texto):
    return all(c.isalpha() or c.isspace() for c in texto)
  
  def preencher_campo(self):
    self.input_nome.insert(0, self.categoria_encontrada.nome)

  def salvar_edicao(self):
      nome = self.input_nome.get().strip()

      if not nome:
        messagebox.showwarning("Erro", "Preencha o campo.")
        return

      self.categoria_encontrada.nome = nome

      try:
          atualizar_categoria_db(self.categoria_encontrada)
          messagebox.showinfo("Sucesso", "Categoria atualizada com sucesso.")
          self.voltar()
      except Exception as e:
          messagebox.showerror("Erro", f"Erro ao atualizar categoria: {e}")
  def voltar(self):
    from interface.produtos.tela_principal import TelaPrincipalProdutos
    self.trocar_tela_callback(TelaPrincipalProdutos, self.usuario_logado)