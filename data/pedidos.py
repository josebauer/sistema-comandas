from data.db_connection import get_connection
from classes.pedido import Pedido
from classes.item_pedido import ItemPedido

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

def atualizar_status_pedido(pedido: Pedido):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    cursor.execute("""
      UPDATE pedido
      SET status = %s, 
      WHERE id = %s
    """, (pedido.nome, pedido.id))

    conn.commit()
  finally:
    cursor.close()
    conn.close()

def consultar_pedido(id: int) -> Pedido | None:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)

  try:
    cursor.execute("SELECT * FROM pedido WHERE id = %s", (id,))
    dados = cursor.fetchone()

    cursor.execute("""
      SELECT nome, obs, valor_unit, qtde, id_produto
      FROM item_pedido
      WHERE id_pedido = %s
    """, (id,))
    itens_data = cursor.fetchall()

    # Criar objetos ItemPedido
    itens = [
        ItemPedido(
            nome=item["nome"],
            observacoes=item["obs"],
            valor_unit=item["valor_unit"],
            quantidade=item["qtde"],
            id_pedido=id,
            id_produto=item["id_produto"]
        )
        for item in itens_data
    ]

    # Retornar o objeto Pedido com os itens
    return Pedido(
        id=dados["id"],
        valor_total=dados["valor_total"],
        status=dados["status"],
        id_metodo_pag=dados["id_metodo_pag"],
        id_usuario=dados["id_usuario"],
        itens=itens
    )

  except Exception as e:
    print(f"Erro ao consultar pedido: {e}")
    return None

  finally:
    cursor.close()
    conn.close()

def listar_pedidos():
  conn = get_connection()
  cursor = conn.cursor()
  
  try:
    cursor.execute("""
      SELECT p.id, p.status, p.valor_total, p.id_metodo_pag, p.id_usuario
      FROM pedido p
    """)
    pedidos_data = cursor.fetchall()

    pedidos = []
    for pd in pedidos_data:
      pedido_id = pd[0]
      cursor.execute("""
        SELECT nome, obs, valor_unit, qtde, id_produto
        FROM item_pedido
        WHERE id_pedido = %s
      """, (pedido_id,))
      itens_data = cursor.fetchall()

      itens = [
        ItemPedido(
          nome=item[0],
          observacoes=item[1],
          valor_unit=item[2],
          quantidade=item[3],
          id_pedido=pedido_id,
          id_produto=item[4]
        )
        for item in itens_data
      ]

      pedido = Pedido(
        id=pedido_id,
        status=pd[1],
        valor_total=pd[2],
        id_metodo_pag=pd[3],
        id_usuario=pd[4],
        itens=itens
      )
      pedidos.append(pedido)

    return pedidos

  except Exception as e:
      print(f"Erro ao listar pedidos: {e}")
      return []

  finally:
      cursor.close()
      conn.close()