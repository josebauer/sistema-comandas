from data.db_connection import get_connection
from classes.usuario import Usuario
from mysql.connector import IntegrityError

usuarios = []

def login_usuario(email: str, senha: str) -> Usuario | None:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)

  try:
    cursor.execute("""
      SELECT * FROM usuario WHERE email = %s AND senha = %s
    """, (email, senha))

    usuario_data = cursor.fetchone()

    if usuario_data:
      return Usuario(
        nome=usuario_data["nome"],
        cpf=usuario_data["cpf"],
        email=usuario_data["email"],
        senha=usuario_data["senha"],
        funcao=usuario_data["funcao"]
      )
    return None

  finally:
    cursor.close()
    conn.close()

def cadastrar_usuario_bd(usuario: Usuario):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      INSERT INTO usuario (nome, cpf, email, senha, funcao)
      VALUES (%s, %s, %s, %s, %s)
    """, (usuario.nome, str(usuario.cpf), usuario.email, usuario.senha, usuario.funcao))

    conn.commit()

  except Exception as e:
    print(f"Erro ao cadastrar usuário: {e}")
    raise
  
  except IntegrityError as e:
    if "Duplicate entry" in str(e):
      raise ValueError("CPF já cadastrado.")
    else:
      raise

  finally:
    cursor.close()
    conn.close()