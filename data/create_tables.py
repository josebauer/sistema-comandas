from db_connection import get_connection

def criar_tabelas():
  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(50) NOT NULL,
      cpf VARCHAR(20) NOT NULL UNIQUE,
      email VARCHAR(50) NOT NULL UNIQUE,
      senha VARCHAR(30) NOT NULL,
      funcao VARCHAR(30) NOT NULL
    );
  """)
  
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(50) NOT NULL
    );
  """)
  
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(50) NOT NULL,
      valor float NOT NULL,
      descricao VARCHAR(100) NOT NULL,
      disponibilidade VARCHAR(20) NOT NULL,
      id_categoria INT NOT NULL,
      FOREIGN KEY (id_categoria) REFERENCES categoria(id)
    );
  """)
  
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS metodo_pag (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(50) NOT NULL
    );
  """)
  
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido (
      id INT AUTO_INCREMENT PRIMARY KEY,
      status VARCHAR(30) NOT NULL,
      valor_total FLOAT NOT NULL,
      id_metodo_pag INT NOT NULL,
      id_usuario INT NOT NULL,
      FOREIGN KEY (id_metodo_pag) REFERENCES metodo_pag(id),
      FOREIGN KEY (id_usuario) REFERENCES usuario(id)
    );
  """)
  
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS item_pedido (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(50) NOT NULL,
      obs VARCHAR(100) NOT NULL,
      valor_unit FLOAT NOT NULL,
      qtde INT NOT NULL,
      id_usuario INT NOT NULL,
      id_produto INT NOT NULL,
      FOREIGN KEY (id_usuario) REFERENCES usuario(id),
      FOREIGN KEY (id_produto) REFERENCES produto(id)
    );
  """)

  conn.commit()
  cursor.close()
  conn.close()
  print("\nTabelas criadas com sucesso.")

if __name__ == "__main__":
  criar_tabelas()