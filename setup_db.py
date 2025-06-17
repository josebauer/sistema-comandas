from data.create_database import criar_banco
from data.create_tables import criar_tabelas
from data.meteodos_pag import cadastrar_met_pag
from classes.metodo_pagamento import MetodoPagamento
from data.usuarios import cadastrar_usuario_db
from classes.usuario import Usuario

def criar_dados_iniciais():
  metodos = ["Dinheiro", "Pix", "Cartão de Débito", "Cartão de Crédito"]
  
  for nome in metodos:
    try:
      cadastrar_met_pag(MetodoPagamento(nome=nome))
    except Exception as e:
      print(f"Método '{nome}' já cadastrado ou erro: {e}")

  try:
    admin = Usuario(
      nome="Administrador",
      cpf="000.000.000-00",
      email="admin@email.com",
      senha="admin",
      funcao="Administrador"
    )
    cadastrar_usuario_db(admin)
  except Exception as e:
    print(f"Usuário admin já cadastrado ou erro: {e}")
  
if __name__ == "__main__":
  criar_banco()
  criar_tabelas()
  criar_dados_iniciais()
  print("Banco de dados configurado com sucesso!")