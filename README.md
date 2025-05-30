<h1 align="center">Sistema de comandas para Cafeteria</h1>

<p align="center">Neste repositório contém o código de um sistema de comandas/pedidos para cafeterias</p>

1. Primeiramente, clone o repositório:
```bash
  git@github.com:josebauer/sistema-comandas.git
```

2. Rode o seguinte código para instalar as dependências do projeto:
```bash
  pip install -r requirements.txt
```

3. Crie o banco de dados com o código a seguir:
```bash
  python data/create_database.py
```

4. Crie as tabelas do banco de dados com o código a seguir:
```bash
  python data/create_tables.py
```

5. Crie o usuário administrador para acessar o sistema, com o código a seguir:
```bash
  python data/create_user_admin.py
```

6. Rode o programa pelo arquivo main ou pelo seguinte código:
```bash
  python main.py
```