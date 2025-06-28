import customtkinter as ctk
import os
from PIL import Image
from utils.caminhos import caminho_recurso
from utils.formatacao import formatar_moeda

class ItemPedidoLista(ctk.CTkFrame):
  def __init__(self, master, pedido, ver_callback, editar_callback, **kwargs):
    super().__init__(master, **kwargs)
    self.pedido = pedido

    cores = {
      'Em preparo': '#a38626',
      'Cancelado': '#cc0000',
      'Entregue': '#238636'
    }
    hover_cores = {
      'Em preparo': '#725e1c',
      'Cancelado': '#701515',
      'Entregue': '#1D5829'
    }

    cor_fundo = cores.get(pedido._status, "#2b2b2b")
    cor_hover = hover_cores.get(pedido._status, "#3a3a3a")

    self.configure(fg_color=cor_fundo, corner_radius=10)

    botoes_frame = ctk.CTkFrame(self, fg_color="transparent")
    botoes_frame.pack(side="right", fill="y", padx=10, pady=10)

    botoes_internos_frame = ctk.CTkFrame(botoes_frame, fg_color="transparent")
    botoes_internos_frame.pack(expand=True)

    icons_path = caminho_recurso("interface/icons")
    icone_ver = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "view.png")), size=(24, 24))
    icone_editar = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "pencil.png")), size=(24, 24))

    ctk.CTkButton(botoes_internos_frame, image=icone_ver, text="", width=40, fg_color="transparent", hover_color=cor_hover, command=lambda: ver_callback(pedido)).pack(side="left", padx=5)

    ctk.CTkButton(botoes_internos_frame, image=icone_editar, text="", width=40, fg_color="transparent", hover_color=cor_hover, command=lambda: editar_callback(pedido)).pack(side="left", padx=5)

    data_formatada = pedido._data_hora.strftime("%d/%m/%Y às %H:%M")
    valor_total_formatado = formatar_moeda(pedido._valor_total)

    ctk.CTkLabel(self, text=f"Pedido nº: {pedido._id} - {pedido._status}", font=ctk.CTkFont(size=14, weight="bold")).pack(side="top", anchor="w", padx=30, pady=(10, 0))

    ctk.CTkLabel(self, text=f"Realizado em: {data_formatada}", font=ctk.CTkFont(size=12, weight="bold")).pack(side="top", anchor="w", padx=30)

    for item in pedido.itens:
      valor_unit_formatado = formatar_moeda(item._valor_unit)
      item_text = f"   - {item._quantidade}x {item._nome} - R$ {valor_unit_formatado}"
      ctk.CTkLabel(self, text=item_text, font=ctk.CTkFont(size=12)).pack(side="top", anchor="w", padx=30, pady=(0, 5))

    ctk.CTkLabel(self, text=f"Total: R${valor_total_formatado}", font=ctk.CTkFont(size=12, weight="bold")).pack(padx=50, pady=(0, 10), anchor="e")