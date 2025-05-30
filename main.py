import customtkinter as ctk
from interface.tela_login import TelaLogin
from interface.tela_gerenciamento import TelaGerenciamento
from classes.usuario import Usuario

DEBUG = True
class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Sistema de Comandas")
    self.geometry("800x600")
    self.resizable(False, False)
    
    self.tela_atual = None
    
    if DEBUG:
      # Usuário de teste para simular um login
      usuario_teste = Usuario(
        nome="Administrador",
        cpf="000.000.000-00",
        email="admin@teste.com",
        senha="1234",
        funcao="Administrador"
      )
      self.trocar_tela(TelaGerenciamento, usuario_teste)
    else:
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