from data.db_connection import get_connection
from classes.categoria import Categoria

def excluir_categoria_db(id: int):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    cursor.execute("DELETE FROM categoria WHERE id = %s", (id,))
    conn.commit()
  finally:
    cursor.close()
    conn.close()
    
def listar_categorias() -> list[Categoria]:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True) 

  try:
    cursor.execute("SELECT * FROM categoria")
    categorias_data = cursor.fetchall()

    return [
      Categoria(
        id=d["id"],
        nome=d["nome"]
      ) for d in categorias_data
    ]

  finally:
    cursor.close()
    conn.close()

def consultar_categoria_db(id: int) -> Categoria | None:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)

  try:
    cursor.execute("SELECT * FROM categoria WHERE id = %s", (id,))
    dados = cursor.fetchone()
    if dados:
      return Categoria(
        id=dados["id"],
        nome=dados["nome"]
      )
    return None
  finally:
    cursor.close()
    conn.close()

def atualizar_categoria_db(categoria: Categoria):
  conn = get_connection()
  cursor = conn.cursor()
  
  try:
    cursor.execute("""
      UPDATE categoria
      SET nome = %s
      WHERE id = %s
    """, (categoria.nome, categoria.id))

    conn.commit()
  finally:
    cursor.close()
    conn.close()

def cadastrar_categoria_db(categoria: Categoria):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      INSERT INTO categoria (nome)
      VALUES (%s)
    """, (categoria.nome,))
    conn.commit()

  except Exception as e:
    print(f"Erro ao cadastrar categoria: {e}")
    raise
  
  finally:
    cursor.close()
    conn.close()