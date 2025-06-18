from data.db_connection import get_connection
from classes.pedido import Pedido

def cadastrar_pedido(pedido: Pedido):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute(
      "INSERT INTO pedido (status, valor_total, id_metodo_pag, id_usuario) VALUES (%s, %s, %s, %s)",
      (pedido._status, pedido._valor_total, pedido._id_metodo_pag, pedido._id_usuario)
    )
    pedido_id = cursor.lastrowid
  
    for item in pedido.itens:
      cursor.execute(
        """
        INSERT INTO item_pedido (nome, obs, valor_unit, qtde, id_pedido, id_produto)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (item._nome, item._observacoes, item._valor_unit, item._quantidade, pedido_id, item._id_produto)
      )

    conn.commit()
    return pedido_id

  except Exception as e:
    conn.rollback()
    print("Erro ao realizar pedido:", e)
    return None

  finally:
    cursor.close()
    conn.close()

  