import customtkinter as ctk
import os
from PIL import Image
from utils.caminhos import caminho_recurso

class ItemPedidoLista(ctk.CTkFrame):
  def __init__(self, master, pedido, ver_callback, editar_callback, **kwargs):
    super().__init__(master, **kwargs)
    self.pedido = pedido

    self.configure(fg_color="#366bac", corner_radius=10)

    texto = f"Pedido nº: {pedido._id} | Status: {pedido._status} | Total: R${pedido._valor_total:.2f}"
    label = ctk.CTkLabel(self, text=texto, font=ctk.CTkFont(size=14, weight="bold"))
    label.pack(side="top", anchor="w", padx=10, pady=(5, 0))
    
    icons_path = caminho_recurso("interface/icons")

    self.icone_editar = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "pencil.png")), size=(24, 24))
    self.icone_ver = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "view.png")), size=(24, 24))
    
    ctk.CTkButton(self, image=self.icone_ver, text="", width=40, fg_color="transparent", hover_color="#204066", command=lambda: ver_callback(pedido)).pack(side="right", padx=5)

    ctk.CTkButton(self, image=self.icone_editar, text="", width=40, fg_color="transparent", hover_color="#204066", command=lambda: editar_callback(pedido)).pack(side="right", padx=5)
    
    for item in pedido.itens:
      item_text = f"   - {item._nome} | Qtd: {item._quantidade} | Valor Unit.: R${item._valor_unit:.2f}"
      ctk.CTkLabel(
        self, text=item_text,
        font=ctk.CTkFont(size=12)
      ).pack(side="top", anchor="w", padx=15, pady=(0, 5))
    