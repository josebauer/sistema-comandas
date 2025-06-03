from data.db_connection import get_connection
from classes.produto import Produto

def cadastrar_produto_bd(produto: Produto):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      INSERT INTO produto (nome, valor, id_categoria, descricao, disponibilidade)
      VALUES (%s, %s, %s, %s, %s)
    """, (produto.nome, str(produto.valor), produto.categoria, produto.descricao, produto.disponibilidade))

    conn.commit()

  except Exception as e:
    print(f"Erro ao cadastrar produto: {e}")
    raise
  
  finally:
    cursor.close()
    conn.close()