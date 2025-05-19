from usuario import Usuario

usuarios = []

# Cria usuário Administrador
admin = Usuario('José H Bauer', 12345678910, 'josebauer@email.com', '1234', 'Administrador')
usuarios.append(admin)

logado = False

def cadastrar_usuario():
  nomeUsuario = input('\nDigite o nome completo: ')
  cpf = int(input('Digite o CPF: '))
  email = input('Digite o email: ')
  senha = input('Insira uma senha forte: ')
  funcao = input('Digite a função (Atendente / Administrador): ')
  
  usuario = Usuario(nomeUsuario, cpf, email, senha, funcao)
  usuarios.append(usuario)
  
  return '\nUsuário cadastrado com sucesso!'

def listar_usuarios():
  if not usuarios:
    print('\nNão há usuários cadastrados.')
  else:
    print('\n----- Usuários Cadastrados -------')
    for usuario in usuarios:
      print(f'\nNome: {usuario._nome}')
      print(f'\nFunção: {usuario._funcao}')
      print('\n----------------------------------')
          
def consultar_usuario():
  if not usuarios:
    print('\nNão há usuários cadastrados.')
  else:
    pesquisa_cpf = int(input('\nInsira o CPF do usuário (Apenas números): '))
    encontrado = False
    
    for usuario in usuarios:
      if usuario._cpf == pesquisa_cpf:
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
    if usuario._cpf == cpf:
      print('\n--- Editar dados do usuário ---')
      print('1 - Nome')
      print('2 - CPF')
      print('3 - Email')
      print('4 - Senha')
      print('5 - Função')
      print('0 - Cancelar')
      opcao = input('\nEscolha a opção que deseja editar: ')

      if opcao == '1':
        novo_nome = input('Novo nome: ')
        usuario._nome = novo_nome
        print('Nome atualizado com sucesso.')
      elif opcao == '2':
        novo_cpf = input('Novo CPF: ')
        usuario._cpf = novo_cpf
        print('CPF atualizado com sucesso.')
      elif opcao == '3':
        novo_email = input('Novo email: ')
        usuario._email = novo_email
        print('Email atualizado com sucesso.')
      elif opcao == '4':
        nova_senha = input('Nova senha: ')
        usuario._senha = nova_senha
        print('Senha atualizada com sucesso.')
      elif opcao == '5':
        nova_funcao = input('Nova função (Atendente / Administrador): ')
        usuario._funcao = nova_funcao
        print('Função atualizada com sucesso.')
      elif opcao == '0':
        print('Edição cancelada.')
      else:
        print('Opção inválida.')

      return
  print('\nUsuário com esse CPF não foi encontrado.')
        
while logado == False:
  print('\n--------- Login ------------\n')
  
  email = input('Digite o seu email: ')
  senha = input('Digite a sua senha: ')
  
  encontrado = False 

  for usuario in usuarios:
    if usuario._email == email and usuario._senha == senha:
      print('\nLogin realizado com sucesso!')
      logado = True
      encontrado = True
      break

  if not encontrado:
      print('\nE-mail ou senha não conferem.')
  
if logado == True:
  while True:
    print('\n--- Gerenciamento de Usuários ---')
    print('\n1 - Cadastrar novo usuário')
    print('\n2 - Ver usuários cadastrados')
    print('\n3 - Consultar pelo CPF')
    print('\n4 - Editar dados usuário')
    print('\n0 - Sair')
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