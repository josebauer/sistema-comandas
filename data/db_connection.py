import mysql.connector
from mysql.connector import Error

def get_connection():
  try:
    conn = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="cafeteria"
    )
    return conn
  except Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    return None