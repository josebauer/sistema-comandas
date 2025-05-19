from usuario import Usuario
import getpass

usuarios = []

# Cria usuário Administrador
admin = Usuario('José H Bauer', 12345678910, 'josebauer@email.com', '1234', 'Administrador')
usuarios.append(admin)

logado = False

def cadastrar_usuario():
  nomeUsuario = input('\nDigite o nome completo: ')
  cpf = int(input('Digite o CPF: '))
  email = input('Digite o email: ')
  senha = getpass.getpass('Insira uma senha forte: ')
  funcao = input('Digite a função (Atendente / Administrador): ')
  
  usuario = Usuario(nomeUsuario, cpf, email, senha, funcao)
  usuarios.append(usuario)
  
  print('\nUsuário cadastrado com sucesso!')

def listar_usuarios():
  if not usuarios:
    print('\nNão há usuários cadastrados.')
  else:
    print('\n----- Usuários Cadastrados -------')
    for usuario in usuarios:
      print(f'\nNome: {usuario.nome}')
      print(f'\nFunção: {usuario.funcao}')
      print('\n----------------------------------')
          
def consultar_usuario():
  if not usuarios:
    print('\nNão há usuários cadastrados.')
  else:
    pesquisa_cpf = int(input('\nInsira o CPF do usuário (Apenas números): '))
    encontrado = False
    
    for usuario in usuarios:
      if usuario.cpf == pesquisa_cpf:
        usuario.ver_dados()
        encontrado = True
    if not encontrado:
      print('\nUsuário não encontrado.')
          
def editar_usuario():
  if not usuarios:
    print('\nNão há usuários cadastrados.')
    return

  cpf = int(input('\nDigite o CPF do usuário que deseja editar: '))
  for usuario in usuarios:
    if usuario.cpf == cpf:
      print('\n--- Editar dados do usuário ---\n')
      print('1 - Nome')
      print('2 - CPF')
      print('3 - Email')
      print('4 - Senha')
      print('5 - Função')
      print('0 - Cancelar')
      opcao = input('\nEscolha a opção que deseja editar: ')

      if opcao == '1':
        usuario.nome = input('Novo nome: ')
        print('Nome atualizado com sucesso.')
      elif opcao == '2':
        usuario.cpf = int(input('Novo CPF: '))
        print('CPF atualizado com sucesso.')
      elif opcao == '3':
        usuario.email = input('Novo email: ')
        print('Email atualizado com sucesso.')
      elif opcao == '4':
        usuario.senha = getpass.getpass('Nova senha: ')
        print('Senha atualizada com sucesso.')
      elif opcao == '5':
        usuario.funcao = input('Nova função (Atendente / Administrador): ')
        print('Função atualizada com sucesso.')
      elif opcao == '0':
        print('Edição cancelada.')
      else:
        print('Opção inválida.')

      return
  print('\nUsuário com esse CPF não foi encontrado.')
  if not usuarios:
    print('\nNão há usuários cadastrados.')

  cpf = int(input('\nDigite o CPF do usuário que deseja editar: '))
  for usuario in usuarios:
    if usuario.cpf == cpf:
      print('\n--- Editar dados do usuário ---\n')
      print('1 - Nome')
      print('2 - CPF')
      print('3 - Email')
      print('4 - Senha')
      print('5 - Função')
      print('0 - Cancelar')
      opcao = input('\nEscolha a opção que deseja editar: ')

      if opcao == '1':
        novo_nome = input('Novo nome: ')
        usuario.nome = novo_nome
        print('\nNome atualizado com sucesso.')
      elif opcao == '2':
        novo_cpf = input('Novo CPF: ')
        usuario.cpf = novo_cpf
        print('\nCPF atualizado com sucesso.')
      elif opcao == '3':
        novo_email = input('Novo email: ')
        usuario.email = novo_email
        print('\nEmail atualizado com sucesso.')
      elif opcao == '4':
        nova_senha = getpass.getpass('Nova senha: ')
        usuario.senha = nova_senha
        print('\nSenha atualizada com sucesso.')
      elif opcao == '5':
        nova_funcao = input('Nova função (Atendente / Administrador): ')
        usuario.funcao = nova_funcao
        print('\nFunção atualizada com sucesso.')
      elif opcao == '0':
        print('\nEdição cancelada.')
      else:
        print('\nOpção inválida.')

      return
  print('\nUsuário com esse CPF não foi encontrado.')
        
while logado == False:
  print('\n--------- Login ------------\n')
  
  email = input('Digite o seu email: ')
  senha = getpass.getpass('Digite a sua senha: ')
  
  encontrado = False 

  for usuario in usuarios:
    if usuario.email == email and usuario.senha == senha:
      print('\nLogin realizado com sucesso!')
      logado = True
      encontrado = True
      break

  if not encontrado:
      print('\nE-mail ou senha não conferem.')
  
if logado == True:
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