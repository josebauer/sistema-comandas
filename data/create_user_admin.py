from db_connection import get_connection

def criar_usuario_admin():
  conn = get_connection()
  cursor = conn.cursor()

  email_admin = 'admin@email.com'
  cpf_admin = '123.456.789-10'

  # Verifica se o usuário já existe pelo email ou CPF
  cursor.execute("""
    SELECT id FROM usuario
    WHERE email = %s OR cpf = %s
  """, (email_admin, cpf_admin))

  resultado = cursor.fetchone()

  if resultado:
    print("\nUsuário administrador já existe.")
  else:
    cursor.execute("""
      INSERT INTO usuario (nome, cpf, email, senha, funcao)
      VALUES (%s, %s, %s, %s, %s)
    """, ('Admin', cpf_admin, email_admin, 'admin', 'Administrador'))

    conn.commit()
    print("\nUsuário administrador criado com sucesso!")

  cursor.close()
  conn.close()

if __name__ == "__main__":
    criar_usuario_admin()







