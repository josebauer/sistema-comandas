<h1 align="center">Sistema de Comandas</h1>

<p align="center">Neste repositório contém o código de um sistema de comandas/pedidos para cafeterias, padarias, fast-foods, etc.
Desenvolvido para o Projeto Integrador, do curso Jovem Programador do SENAC-SC</p>

1. Primeiramente, clone o repositório:
```bash
  git@github.com:josebauer/sistema-comandas.git
```

2. Entre na pasta do projeto:
```bash
  cd .\sistema-comandas\
```

3. Rode o seguinte código para instalar as dependências do projeto:
```bash
  pip install -r requirements.txt
```

4. Crie o banco de dados com o código a seguir:
```bash
  python data/create_database.py
```

5. Crie as tabelas do banco de dados com o código a seguir:
```bash
  python data/create_tables.py
```

6. Crie o usuário administrador para acessar o sistema, com o código a seguir:
```bash
  python data/create_user_admin.py
```

7. Rode o programa pelo arquivo main ou pelo seguinte código:
```bash
  python main.py
```