from data.db_connection import get_connection
from classes.categoria import Categoria

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

def cadastrar_categoria_bd(categoria: Categoria):
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