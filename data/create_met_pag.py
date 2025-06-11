from db_connection import get_connection

def criar_met_pag():
  conn = get_connection()
  cursor = conn.cursor()

  metodos_pagamento = ['Dinheiro', 'Pix', 'Cartão de Débito', 'Cartão de Crédito']

  for nome in metodos_pagamento:
    cursor.execute("""
      SELECT id FROM metodo_pag WHERE nome = %s
    """, (nome,))
    resultado = cursor.fetchone()

    if resultado:
      print(f"Método de pagamento '{nome}' já existe.")
    else:
      cursor.execute("""
        INSERT INTO metodo_pag (nome)
        VALUES (%s)
      """, (nome,))
      print(f"Método de pagamento '{nome}' inserido com sucesso.")

  conn.commit()
  cursor.close()
  conn.close()

if __name__ == "__main__":
    criar_met_pag()