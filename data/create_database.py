import mysql.connector
from mysql.connector import Error

def criar_banco():
  try:
    conn = mysql.connector.connect(
      host='localhost',
      user='root',
      password='root' 
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS cafeteria")
    print("Banco de dados criado (ou já existia).")

    cursor.close()
    conn.close()

  except Error as e:
    print(f"Erro ao criar banco de dados: {e}")

if __name__ == "__main__":
  criar_banco()