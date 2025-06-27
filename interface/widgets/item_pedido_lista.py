import customtkinter as ctk
import os
from PIL import Image
from utils.caminhos import caminho_recurso
from utils.formatacao import formatar_moeda

class ItemPedidoLista(ctk.CTkFrame):
  def __init__(self, master, pedido, ver_callback, editar_callback, **kwargs):
    super().__init__(master, **kwargs)
    self.pedido = pedido

    self.configure(fg_color="#366bac", corner_radius=10)
    
    data_formatada = pedido._data_hora.strftime("%d/%m/%Y às %H:%M")
    valor_total_formatado = formatar_moeda(pedido._valor_total)

    texto = f"Pedido nº: {pedido._id} - {pedido._status}"
    label = ctk.CTkLabel(self, text=texto, font=ctk.CTkFont(size=14, weight="bold"))
    label.pack(side="top", anchor="w", padx=30, pady=(10, 0))
    
    label_data_hora = ctk.CTkLabel(self, text=f"Realizado em: {data_formatada}", font=ctk.CTkFont(size=12, weight="bold"))
    label_data_hora.pack(side="top", anchor="w", padx=30)
    
    icons_path = caminho_recurso("interface/icons")

    self.icone_editar = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "pencil.png")), size=(24, 24))
    self.icone_ver = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "view.png")), size=(24, 24))
    
    ctk.CTkButton(self, image=self.icone_ver, text="", width=40, fg_color="transparent", hover_color="#204066", command=lambda: ver_callback(pedido)).pack(side="right", padx=5)

    ctk.CTkButton(self, image=self.icone_editar, text="", width=40, fg_color="transparent", hover_color="#204066", command=lambda: editar_callback(pedido)).pack(side="right", padx=5)
    
    for item in pedido.itens:
      valor_unit_formatado = formatar_moeda(item._valor_unit)
      item_text = f"   - {item._nome} | Qtd: {item._quantidade} | Valor Unit.: R$ {valor_unit_formatado}"
      ctk.CTkLabel(
        self, text=item_text,
        font=ctk.CTkFont(size=12)
      ).pack(side="top", anchor="w", padx=30, pady=(0, 5))
    
    label_valor_total = ctk.CTkLabel(self, text=f"Total: R${valor_total_formatado}", font=ctk.CTkFont(size=12, weight="bold"))