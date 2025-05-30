from data.db_connection import get_connection
from classes.usuario import Usuario
from mysql.connector import IntegrityError

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
        id=usuario_data["id"],
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

def excluir_usuario_db(id: int):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    conn.commit()
  finally:
    cursor.close()
    conn.close()

def listar_usuarios() -> list[Usuario]:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True) 

  try:
    cursor.execute("SELECT * FROM usuario")
    usuarios_data = cursor.fetchall()

    return [
      Usuario(
        id=d["id"],
        nome=d["nome"],
        cpf=d["cpf"],
        email=d["email"],
        senha=d["senha"],
        funcao=d["funcao"]
      ) for d in usuarios_data
    ]

  finally:
    cursor.close()
    conn.close()

def consultar_usuario_db(id: int) -> Usuario | None:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)

  try:
    cursor.execute("SELECT * FROM usuario WHERE id = %s", (id,))
    dados = cursor.fetchone()
    if dados:
      return Usuario(
        id=dados["id"],
        nome=dados["nome"],
        cpf=dados["cpf"],
        email=dados["email"],
        senha=dados["senha"],
        funcao=dados["funcao"]
      )
    return None
  finally:
    cursor.close()
    conn.close()

def atualizar_usuario_db(usuario: Usuario):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      UPDATE usuario
      SET nome = %s, email = %s, senha = %s, funcao = %s
      WHERE id = %s
    """, (usuario.nome, usuario.email, usuario.senha, usuario.funcao, usuario.id))

    conn.commit()
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