# Importa as funcoes do programa
from functions.autenticar import login
from functions.cadastrar_usuario import cadastrar_usuario
from functions.consultar_usuarios import listar_usuarios, consultar_usuario
from functions.editar_usuario import editar_usuario
from data.usuarios import usuarios

'''
    Fazer o login com as seguintes credenciais:
    
    E-mail: josebauer@email.com
    Senha: 1234
'''

# Exibe menu para gerenciar usuários
def gerenciar_usuarios():
    while True:
      print('\n--- Gerenciamento de Usuários ---\n')
      print('1 - Cadastrar novo usuário')
      print('2 - Ver usuários cadastrados')
      print('3 - Consultar pelo CPF')
      print('4 - Editar dados usuário')
      print('0 - Sair')
      print('\n---------------------------------')

      opcao = int(input('\nEscolha uma opção: '))
      if opcao == 0:
          break
      elif opcao == 1:
          cadastrar_usuario()
      elif opcao == 2:
          listar_usuarios()
      elif opcao == 3:
          consultar_usuario()
      elif opcao == 4:
          editar_usuario()
      else:
          print('\nOpção Inválida.')

if __name__ == "__main__":
    usuario_logado = login()
    if usuario_logado and usuario_logado.funcao == "Administrador":
        gerenciar_usuarios()