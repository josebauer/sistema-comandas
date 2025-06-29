from data.db_connection import get_connection
from classes.pedido import Pedido
from classes.item_pedido import ItemPedido

def cadastrar_pedido(pedido: Pedido):
  conn = get_connection()
  cursor = conn.cursor()
  
  try:
    cursor.execute(
      "INSERT INTO pedido (data_hora, status, valor_total, id_metodo_pag, id_usuario) VALUES (%s, %s, %s, %s, %s)",
      (pedido._data_hora, pedido._status, pedido._valor_total, pedido._id_metodo_pag, pedido._id_usuario)
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
      SET status = %s
      WHERE id = %s
    """, (pedido._status, pedido._id))

    conn.commit()
  finally:
    cursor.close()
    conn.close()

def consultar_pedido(id: int) -> Pedido | None:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)

  try:
    cursor.execute("""
      SELECT p.*, u.nome AS nome_usuario, m.nome AS nome_met_pag
      FROM pedido p
      JOIN usuario u ON p.id_usuario = u.id
      JOIN metodo_pag m ON p.id_metodo_pag = m.id
      WHERE p.id = %s
    """, (id,))
    dados = cursor.fetchone()

    cursor.execute("""
      SELECT nome, obs, valor_unit, qtde, id_produto
      FROM item_pedido
      WHERE id_pedido = %s
    """, (id,))
    itens_data = cursor.fetchall()

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

    return Pedido(
        id=dados["id"],
        data_hora=dados["data_hora"],
        valor_total=dados["valor_total"],
        status=dados["status"],
        id_metodo_pag=dados["id_metodo_pag"],
        id_usuario=dados["id_usuario"],
        itens=itens,
        nome_usuario=dados["nome_usuario"],
        nome_metodo_pagamento=dados["nome_met_pag"]
    )

  except Exception as e:
    print(f"Erro ao consultar pedido: {e}")
    return None

  finally:
    cursor.close()
    conn.close()

def listar_pedidos_por_status(status):
  conn = get_connection()
  cursor = conn.cursor()
  
  try:
    cursor.execute("""
      SELECT p.id, p.data_hora, p.status, p.valor_total, p.id_metodo_pag, p.id_usuario
      FROM pedido p 
      WHERE p.status = %s
      ORDER BY p.data_hora DESC
    """, (status,))
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
        data_hora=pd[1],
        status=pd[2],
        valor_total=pd[3],
        id_metodo_pag=pd[4],
        id_usuario=pd[5],
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

def listar_pedidos():
  conn = get_connection()
  cursor = conn.cursor()
  
  try:
    cursor.execute("""
      SELECT p.id, p.data_hora, p.status, p.valor_total, p.id_metodo_pag, p.id_usuario
      FROM pedido p
      ORDER BY p.data_hora DESC
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
        data_hora=pd[1],
        status=pd[2],
        valor_total=pd[3],
        id_metodo_pag=pd[4],
        id_usuario=pd[5],
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