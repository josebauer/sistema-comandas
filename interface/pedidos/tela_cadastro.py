import customtkinter as ctk
from tkinter import messagebox
from data.produtos import listar_produtos_disponiveis
from data.meteodos_pag import listar_met_pag
from data.pedidos import cadastrar_pedido
from classes.pedido import Pedido
from classes.item_pedido import ItemPedido
from interface.widgets.item_pedido import ItemPedidoWidget
from datetime import datetime

class TelaCadastroPedido(ctk.CTkFrame):
  def __init__(self, master, trocar_tela_callback, usuario_logado):
    super().__init__(master)
    self.usuario_logado = usuario_logado
    self.trocar_tela_callback = trocar_tela_callback
    self.itens_pedido = []

    self.frame = ctk.CTkFrame(self, fg_color="transparent")
    self.frame.pack(expand=True)

    ctk.CTkLabel(self.frame, text="Cadastro de Pedido", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 20))

    # Produtos disponíveis
    self.produtos_disponiveis = listar_produtos_disponiveis()
    self.produtos_dict = {f"{p.nome} - R${p.valor:.2f}": p for p in self.produtos_disponiveis}

    self.combo_produto = ctk.CTkOptionMenu(
      self.frame, 
      values=list(self.produtos_dict.keys()),
      fg_color="#366bac",
      button_color="#204066",  
      button_hover_color="#366bac",
      height=40,
      width=400
    )
    if self.produtos_disponiveis:
      self.combo_produto.set("Selecione um produto")
    self.combo_produto.pack(pady=5)

    self.input_quantidade = ctk.CTkEntry(self.frame, placeholder_text="Quantidade", height=40, width=400)
    self.input_quantidade.pack(pady=5)

    self.input_observacao = ctk.CTkEntry(self.frame, placeholder_text="Observações (opcional)", height=40, width=400)
    self.input_observacao.pack(pady=5)
    
    self.item_em_edicao = None

    self.botao_adicionar = ctk.CTkButton(
        self.frame, text="Adicionar Item",
        command=self.adicionar_item,
        height=40,
        fg_color="transparent",
        font=ctk.CTkFont(size=14, weight="bold"),
        border_width=2,
        border_color="#238636",
        hover_color="#238636"
    )
    self.botao_adicionar.pack(pady=(5, 15))

    # Lista de itens do pedido
    self.scroll_frame_itens = ctk.CTkScrollableFrame(self.frame, width=400, height=200)
    self.scroll_frame_itens.pack(pady=5)
    
    # Lista de métodos de pagamento
    self.metodos_pag = listar_met_pag()
    self.metodos_pag_dict = {f"{m.nome}": m for m in self.metodos_pag}
    self.combo_met_pag = ctk.CTkOptionMenu(
      self.frame, 
      values=list(self.metodos_pag_dict.keys()), 
      fg_color="#366bac",
      button_color="#204066",  
      button_hover_color="#366bac",
      height=40,
      width=400
    )
    
    if self.metodos_pag:
      self.combo_met_pag.set("Selecione o método de pagamento")
    self.combo_met_pag.pack(pady=5)

    # Botões de ação
    botoes_frame = ctk.CTkFrame(self.frame)
    botoes_frame.pack(pady=(15, 0), fill="x")

    ctk.CTkButton(
      botoes_frame, text="Finalizar Pedido",
      command=self.finalizar_pedido,
      height=40,
      fg_color="transparent", border_width=2,
      font=ctk.CTkFont(size=14, weight="bold"),
      border_color="#238636", hover_color="#238636"
    ).pack(side="left", expand=True, fill="x", padx=(0, 5))

    ctk.CTkButton(
      botoes_frame, text="Voltar",
      command=self.voltar,
      height=40,
      fg_color="transparent", border_width=2,
      font=ctk.CTkFont(size=14, weight="bold"),
      border_color="#63a9ff", hover_color="#63a9ff"
    ).pack(side="left", expand=True, fill="x", padx=(5, 0))

  def adicionar_item(self):
    produto_nome = self.combo_produto.get()
    produto = self.produtos_dict.get(produto_nome)
    quantidade = self.input_quantidade.get()
    observacao = self.input_observacao.get()

    if not produto or produto_nome == "Selecione um produto":
      messagebox.showwarning("Erro", "Selecione um produto válido.")
      return

    try:
      quantidade = int(quantidade)
      if quantidade <= 0:
        raise ValueError
    except ValueError:
      messagebox.showwarning("Erro", "Quantidade inválida.")
      return

    if self.item_em_edicao:
        # Está editando um item
      self.item_em_edicao._nome = produto.nome
      self.item_em_edicao._valor_unit = produto.valor
      self.item_em_edicao._id_produto = produto.id
      self.item_em_edicao._quantidade = quantidade
      self.item_em_edicao._observacoes = observacao

      self.item_em_edicao = None
      self.botao_adicionar.configure(text="Adicionar Item")
    else:
      # Adicionando novo item
      item_existente = next((i for i in self.itens_pedido if i._id_produto == produto.id), None)

      if item_existente:
        item_existente._quantidade += quantidade
        item_existente._observacoes = observacao or item_existente._observacoes
        messagebox.showinfo("Atualizado", "O item já estava no pedido. A quantidade foi atualizada.")
      else:
        item = ItemPedido(
          nome=produto.nome,
          observacoes=observacao,
          valor_unit=produto.valor,
          quantidade=quantidade,
          id_pedido=None,
          id_produto=produto.id
        )
        self.itens_pedido.append(item)
    self.atualizar_lista_itens()

    # Limpar campos
    self.combo_produto.set("Selecione um produto")
    self.input_quantidade.delete(0, "end")
    self.input_observacao.delete(0, "end")

  def editar_item(self, item):
    self.item_em_edicao = item

    # Preencher os inputs com os dados do item
    produto_nome = next(
        (nome for nome, prod in self.produtos_dict.items() if prod.id == item._id_produto),
        None
    )
    if produto_nome:
        self.combo_produto.set(produto_nome)

    self.input_quantidade.delete(0, "end")
    self.input_quantidade.insert(0, str(item._quantidade))

    self.input_observacao.delete(0, "end")
    self.input_observacao.insert(0, item._observacoes or "")

    self.botao_adicionar.configure(text="Salvar Alteração")

  def excluir_item(self, item):
    self.itens_pedido.remove(item)
    self.atualizar_lista_itens()
    
  def atualizar_lista_itens(self):
    for widget in self.scroll_frame_itens.winfo_children():
        widget.destroy()

    for item in self.itens_pedido:
      widget = ItemPedidoWidget(
        self.scroll_frame_itens,
        item_pedido=item,
        editar_callback=self.editar_item,
        excluir_callback=self.excluir_item
      )
      widget.pack(fill="x", padx=5, pady=2)

  def finalizar_pedido(self):
    
    data_hora = datetime.now()
      
    metodo_pag = self.combo_met_pag.get()
    
    if not self.itens_pedido:
      messagebox.showwarning("Erro", "Adicione ao menos um item ao pedido.")
      return

    metodo_pag_nome = self.combo_met_pag.get()
    metodo_pag = self.metodos_pag_dict.get(metodo_pag_nome)
    if not metodo_pag:
      messagebox.showwarning("Erro", "Selecione um método de pagamento válido.")
      return

    valor_total = sum(item._valor_unit * item._quantidade for item in self.itens_pedido)
    pedido = Pedido(
      data_hora=data_hora,
      valor_total=valor_total,
      status="Em preparo",
      id_metodo_pag=metodo_pag.id,
      id_usuario=self.usuario_logado.id,
      itens=self.itens_pedido
    )

    try:
      cadastrar_pedido(pedido)
      pedido._id = cadastrar_pedido(pedido)
      messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso.")
      self.itens_pedido.clear()
      self.atualizar_lista_itens()
      self.combo_met_pag.set("Selecione o método de pagamento")
      
      from interface.pedidos.tela_consulta import TelaConsultaPedido
      self.trocar_tela_callback(TelaConsultaPedido, self.usuario_logado, pedido._id)
    except Exception as e:
      messagebox.showerror("Erro", f"Erro ao cadastrar pedido: {e}")

  def voltar(self):
    if self.usuario_logado.funcao == 'Administrador':
      from interface.tela_gerenciamento import TelaGerenciamento
      self.trocar_tela_callback(TelaGerenciamento, self.usuario_logado)
    else:
      from interface.tela_atendente import TelaAtendente
      self.trocar_tela_callback(TelaAtendente, self.usuario_logado)
