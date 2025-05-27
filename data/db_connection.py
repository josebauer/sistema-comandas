import mysql.connector

# Estabelecendo conexão
conexao = mysql.connector.connect(
    host="localhost",        # ou IP do servidor
    user="root",      # substitua pelo seu usuário
    password="root",    # substitua pela sua senha
    database="cafeteria" # nome do banco de dados
)

cursor = conexao.cursor()

# Exemplo de comando SQL
cursor.execute("SELECT * FROM usuario")

# Pegar resultados
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# Encerrar conexão
cursor.close()
conexao.close()


