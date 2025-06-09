import customtkinter as ctk
from tkinter import messagebox
from data.produtos import listar_produtos_disponiveis
from data.pedidos import cadastrar_pedido
from classes.pedido import Pedido
from classes.item_pedido import ItemPedido
from interface.widgets.item_pedido import ItemPedidoWidget

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

    self.combo_produto = ctk.CTkOptionMenu(self.frame, values=list(self.produtos_dict.keys()), width=400)
    if self.produtos_disponiveis:
      self.combo_produto.set("Selecione um produto")
    self.combo_produto.pack(pady=5)

    self.input_quantidade = ctk.CTkEntry(self.frame, placeholder_text="Quantidade", width=400)
    self.input_quantidade.pack(pady=5)

    self.input_observacao = ctk.CTkEntry(self.frame, placeholder_text="Observações (opcional)", width=400)
    self.input_observacao.pack(pady=5)

    ctk.CTkButton(self.frame, text="Adicionar Item", command=self.adicionar_item).pack(pady=(5, 15))

    # Lista de itens do pedido
    self.scroll_frame_itens = ctk.CTkScrollableFrame(self.frame, width=400, height=200)
    self.scroll_frame_itens.pack(pady=5)

    # Botões de ação
    botoes_frame = ctk.CTkFrame(self.frame)
    botoes_frame.pack(pady=(15, 0), fill="x")

    ctk.CTkButton(
      botoes_frame, text="Finalizar Pedido",
      command=self.finalizar_pedido,
      fg_color="transparent", border_width=2,
      border_color="#238636", hover_color="#238636"
    ).pack(side="left", expand=True, fill="x", padx=(0, 5))

    ctk.CTkButton(
      botoes_frame, text="Voltar",
      command=self.voltar,
      fg_color="transparent", border_width=2,
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

    item = ItemPedido(
      nome=produto.nome,
      observacoes=observacao,
      valor_unit=produto.valor,
      quantidade=quantidade
    )
    self.itens_pedido.append(item)

    self.atualizar_lista_itens()

    # Limpar campos
    self.input_quantidade.delete(0, "end")
    self.input_observacao.delete(0, "end")

  def editar_item(self, item):
    nova_qtd = ctk.CTkInputDialog(title="Editar Quantidade", text="Nova quantidade:").get_input()
    try:
        nova_qtd = int(nova_qtd)
        if nova_qtd <= 0:
            raise ValueError
        item._quantidade = nova_qtd
        self.atualizar_lista_itens()
    except:
        messagebox.showwarning("Erro", "Quantidade inválida.")

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
    if not self.itens_pedido:
      messagebox.showwarning("Erro", "Adicione ao menos um item ao pedido.")
      return

    valor_total = sum(item._valor_unit * item._quantidade for item in self.itens_pedido)
    pedido = Pedido(valor_total=valor_total, status="Pendente")

    try:
      cadastrar_pedido(self, pedido)
      messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso.")
      self.itens_pedido.clear()
      self.atualizar_lista_itens()
    except Exception as e:
      messagebox.showerror("Erro", f"Erro ao cadastrar pedido: {e}")

  def voltar(self):
    from interface.pedidos.tela_principal import TelaPrincipalPedidos
    self.trocar_tela_callback(TelaPrincipalPedidos, self.usuario_logado)
