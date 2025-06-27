import os
from PIL import Image
import customtkinter as ctk
from utils.caminhos import caminho_recurso
from utils.formatacao import formatar_moeda

class ItemPedidoWidget(ctk.CTkFrame):
  def __init__(self, master, item_pedido, editar_callback, excluir_callback, **kwargs):
    super().__init__(master, **kwargs)
    self.item_pedido = item_pedido

    self.configure(fg_color="#3b3b3b", corner_radius=10)
    valor_unit_formatado = formatar_moeda(item_pedido._valor_unit)

    label_nome = ctk.CTkLabel(
      self,
      text=f"{item_pedido._quantidade}x {item_pedido._nome} - R$ {valor_unit_formatado}",
      font=ctk.CTkFont(size=14, weight="bold"),
      anchor="w"
    )
    label_nome.pack(side="left", padx=10, pady=10, expand=True)

    icons_path = caminho_recurso("interface/icons")

    icone_editar = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "pencil.png")), size=(24, 24))
    icone_excluir = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "trash.png")), size=(24, 24))

    ctk.CTkButton(
      self,
      image=icone_editar,
      text="",
      width=40,
      fg_color="transparent",
      hover_color="#204066",
      command=lambda: editar_callback(item_pedido)
    ).pack(side="right", padx=5)

    ctk.CTkButton(
      self,
      image=icone_excluir,
      text="",
      width=40,
      fg_color="transparent",
      hover_color="#204066",
      command=lambda: excluir_callback(item_pedido)
    ).pack(side="right", padx=5)