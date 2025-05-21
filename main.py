from PyQt5.QtWidgets import QApplication
from gui.janela_login import JanelaLogin
import sys

'''
  Fazer o login com as seguintes credenciais:
  
  E-mail: josebauer@email.com
  Senha: 1234
  
'''

app = QApplication(sys.argv)

janela_login = JanelaLogin()
janela_login.show()

sys.exit(app.exec_())