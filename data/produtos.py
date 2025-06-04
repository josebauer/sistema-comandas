from data.db_connection import get_connection
from classes.produto import Produto

def excluir_produto_db(id: int):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    cursor.execute("DELETE FROM produto WHERE id = %s", (id,))
    conn.commit()
  finally:
    cursor.close()
    conn.close()

def atualizar_produto_db(produto: Produto):
  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      UPDATE produto
      SET nome = %s, valor = %s, id_categoria = %s, descricao = %s, disponibilidade = %s
      WHERE id = %s
    """, (produto.nome, produto.valor, produto.id_categoria, produto.descricao, produto.disponibilidade, produto.id))

    conn.commit()
  finally:
    cursor.close()
    conn.close()

def consultar_produto_db(id: int) -> Produto | None:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)

  try:
    cursor.execute("SELECT * FROM produto WHERE id = %s", (id,))
    dados = cursor.fetchone()
    if dados:
      return Produto(
        id=dados["id"],
        nome=dados["nome"],
        valor=dados["valor"],
        id_categoria=dados["id_categoria"],
        descricao=dados["descricao"],
        disponibilidade=dados["disponibilidade"]
      )
    return None
  finally:
    cursor.close()
    conn.close()

def listar_produtos() -> list[Produto]:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True) 

  try:
    cursor.execute("SELECT * FROM produto")
    produtos_data = cursor.fetchall()

    return [
      Produto(
        id=d["id"],
        nome=d["nome"],
        valor=d["valor"],
        id_categoria=d["id_categoria"],
        descricao=d["descricao"],
        disponibilidade=d["disponibilidade"]
      ) for d in produtos_data
    ]

  finally:
    cursor.close()
    conn.close()

def cadastrar_produto_db(produto: Produto):

  conn = get_connection()
  cursor = conn.cursor()

  try:
    cursor.execute("""
      INSERT INTO produto (nome, valor, id_categoria, descricao, disponibilidade)
      VALUES (%s, %s, %s, %s, %s)
    """, (produto.nome, produto.valor, produto.id_categoria, produto.descricao, produto.disponibilidade))

    conn.commit()

  except Exception as e:
    print(f"Erro ao cadastrar produto: {e}")
    raise
  
  finally:
    cursor.close()
    conn.close()