from data.usuarios import usuarios

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
    return

  cpf = int(input('\nInsira o CPF do usuário: '))
  for usuario in usuarios:
    if usuario.cpf == cpf:
      usuario.ver_dados()
      return
  print('\nUsuário não encontrado.')