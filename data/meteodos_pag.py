from data.db_connection import get_connection
from classes.metodo_pagamento import MetodoPagamento

def listar_met_pag() -> list[MetodoPagamento]:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True) 

  try:
    cursor.execute("SELECT * FROM metodo_pag")
    met_pag_data = cursor.fetchall()

    return [
      MetodoPagamento(
        id=d["id"],
        nome=d["nome"]
      ) for d in met_pag_data
    ]

  finally:
    cursor.close()
    conn.close()

def cadastrar_met_pag(metodo_pag: MetodoPagamento):
  conn = get_connection()
  cursor = conn.cursor()
  
  try:
    cursor.execute("""
      INSERT INTO metodo_pag (nome)
      VALUES (%s)
    """, (metodo_pag.nome,))
    conn.commit()

  except Exception as e:
    print(f"Erro ao cadastrar método de pagamento: {e}")
    raise
  
  finally:
    cursor.close()
    conn.close()