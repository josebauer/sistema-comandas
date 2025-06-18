import customtkinter as ctk
from interface.tela_login import TelaLogin
from interface.tela_gerenciamento import TelaGerenciamento
from classes.usuario import Usuario

DEBUG = False
class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Sistema de Comandas")
    self.geometry("800x600")
    
    self.tela_atual = None
    
    self.trocar_tela(TelaLogin)

  def trocar_tela(self, TelaClasse, *args):
    if self.tela_atual:
      self.tela_atual.destroy()
    self.tela_atual = TelaClasse(self, self.trocar_tela, *args)
    self.tela_atual.pack(fill="both", expand=True)

if __name__ == "__main__":
  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("green")

  app = App()
  app.mainloop()