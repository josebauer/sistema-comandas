from getpass import getpass
from data.usuarios import usuarios

def login():
  while True:
    print('\n--------- Login ------------\n')
    email = input('Digite o seu email: ')
    senha = getpass('Digite a sua senha: ')

    for usuario in usuarios:
      if usuario.email == email and usuario.senha == senha:
        print('\nLogin realizado com sucesso!')
        return usuario

    print('\nE-mail ou senha não conferem.')