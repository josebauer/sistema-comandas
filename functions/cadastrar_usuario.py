from classes.usuario import Usuario
from getpass import getpass
from data.usuarios import usuarios

def cadastrar_usuario():
  nome = input('\nDigite o nome completo: ')
  cpf = int(input('Digite o CPF (Apenas números): '))
  email = input('Digite o email: ')
  senha = getpass('Insira uma senha forte: ')
  funcao = input('Digite a função (Atendente / Administrador): ')
  
  usuario = Usuario(nome, cpf, email, senha, funcao)
  usuarios.append(usuario)
  print('\nUsuário cadastrado com sucesso!')