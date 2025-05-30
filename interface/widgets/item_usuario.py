import os
from PIL import Image
import customtkinter as ctk

class ItemUsuario(ctk.CTkFrame):
  def __init__(self, master, usuario, ver_callback, editar_callback, excluir_callback, **kwargs):
    super().__init__(master, **kwargs)
    self.usuario = usuario

    self.configure(fg_color="#cc0000", corner_radius=10)

    label_nome = ctk.CTkLabel(self, text=usuario.nome, font=ctk.CTkFont(size=14, weight="bold"))
    label_nome.pack(side="left", padx=(10, 0), pady=10, expand=True)
 
    base_path = os.path.dirname(__file__)
    icons_path = os.path.join(base_path, "..", "icons") 
        
    self.icone_editar = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "pencil.png")), size=(24, 24))
    self.icone_excluir = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "trash.png")), size=(24, 24))
    self.icone_ver = ctk.CTkImage(light_image=Image.open(os.path.join(icons_path, "view.png")), size=(24, 24))
    
    # Botões de ação
    ctk.CTkButton(self, image=self.icone_ver, text="", width=40, fg_color="transparent", hover_color="#900", command=lambda: ver_callback(usuario)).pack(side="right", padx=5)

    ctk.CTkButton(self, image=self.icone_editar, text="", width=40, fg_color="transparent", hover_color="#900", command=lambda: editar_callback(usuario)).pack(side="right", padx=5)

    ctk.CTkButton(self, image=self.icone_excluir, text="",  width=40, fg_color="transparent", hover_color="#900", command=lambda: excluir_callback(usuario)).pack(side="right", padx=5)