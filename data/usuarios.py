from classes.usuario import Usuario

usuarios = []

admin = Usuario(
  nome='José H Bauer',
  cpf=12345678910,
  email='josebauer@email.com',
  senha='1234',
  funcao='Administrador'
)

usuarios.append(admin)