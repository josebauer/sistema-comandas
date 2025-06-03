from data.db_connection import get_connection
from classes.categoria import Categoria

def cadastrar_categoria_bd(categoria: Categoria):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      INSERT INTO categoria (nome)
      VALUES (%s)
    """, (categoria.nome))
    conn.commit()

  except Exception as e:
    print(f"Erro ao cadastrar categoria: {e}")
    raise
  
  finally:
    cursor.close()
    conn.close()