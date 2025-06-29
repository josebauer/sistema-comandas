import os
from PIL import Image
import customtkinter as ctk
from utils.caminhos import caminho_recurso

class ItemCategoria(ctk.CTkFrame):
  def __init__(self, master, categoria, ver_callback, editar_callback, excluir_callback, **kwargs):
    super().__init__(master, **kwargs)
    self.categoria = categoria

    self.configure(fg_color="#366bac", corner_radius=10)

    label_nome = ctk.CTkLabel(
      self,
      text=categoria.nome,
      font=ctk.CTkFont(size=14, weight="bold")
    )
    label_nome.pack(side="left", padx=(10, 0), pady=10, expand=True)

    icons_path = caminho_recurso("interface/icons")

    self.icone_editar = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "pencil.png")), size=(24, 24))
    self.icone_excluir = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "trash.png")), size=(24, 24))

    # Botões de ação
    ctk.CTkButton(
      self,
      image=self.icone_editar,
      text="",
      width=40,
      fg_color="transparent",
      hover_color="#204066",
      command=lambda: editar_callback(categoria)
    ).pack(side="right", padx=5)

    ctk.CTkButton(
      self,
      image=self.icone_excluir,
      text="",
      width=40,
      fg_color="transparent",
      hover_color="#204066",
      command=lambda: excluir_callback(categoria)
    ).pack(side="right", padx=5)
