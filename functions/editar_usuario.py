from getpass import getpass
from data.usuarios import usuarios

def editar_usuario():
  cpf = int(input('\nDigite o CPF do usuário que deseja editar: '))
  for usuario in usuarios:
    if usuario.cpf == cpf:
      print('\n--- Editar dados do usuário ---')
      print('1 - Nome\n2 - CPF\n3 - Email\n4 - Senha\n5 - Função\n0 - Cancelar')
      opcao = input('Escolha a opção que deseja editar: ')

      if opcao == '1':
          usuario.nome = input('Novo nome: ')
      elif opcao == '2':
          usuario.cpf = int(input('Novo CPF: '))
      elif opcao == '3':
          usuario.email = input('Novo email: ')
      elif opcao == '4':
          usuario.senha = getpass('Nova senha: ')
      elif opcao == '5':
          usuario.funcao = input('Nova função: ')
      elif opcao == '0':
          print('Edição cancelada.')
          return
      else:
          print('Opção inválida.')
          return

      print('Informação atualizada com sucesso.')
      return
  print('\nUsuário não encontrado.')