from data.db_connection import get_connection
from classes.pedido import Pedido

def cadastrar_pedido(pedido: Pedido):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute(
      "INSERT INTO pedido (valor_total, status) VALUES (%s, %s)",
      (pedido._valor_total, pedido._status)
    )
    pedido_id = cursor.lastrowid
  
    for item in pedido.itens:
      cursor.execute(
        """
        INSERT INTO item_pedido (pedido_id, nome, observacoes, valor_unit, quantidade)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (pedido_id, item._nome, item._observacoes, item._valor_unit, item._quantidade)
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
  
  