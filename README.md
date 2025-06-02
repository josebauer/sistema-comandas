<h1 align="center">Sistema de Comandas</h1>

<p align="center">Neste repositório contém o código de um sistema de comandas/pedidos para cafeterias, padarias, fast-foods, etc.
Desenvolvido para o Projeto Integrador, do curso Jovem Programador do SENAC-SC. <a href="https://senacsc754.sharepoint.com/:w:/s/174292711002620252510001.sc.senac.br-EquipedoPI6/ES7Au0teNz9Jj2Yvws_jMNEBm0h5SljkomeAazTx-zQmvA?e=Rx1FyJ">Ver Documentação</a>.</p>


<h3>1. Primeiramente, clone o repositório:</h3>

  - HTTPS:
```bash
  https://github.com/josebauer/sistema-comandas.git
```
  - SSH:
```bash
  git@github.com:josebauer/sistema-comandas.git
```

<h3>2. Entre na pasta do projeto:</h3>

```bash
  cd .\sistema-comandas\
```

<h3>3. Rode o seguinte código para instalar as dependências do projeto:</h3>

```bash
  pip install -r requirements.txt
```

<h3>4. Crie o banco de dados com o código a seguir:</h3>

```bash
  python data/create_database.py
```

<h3>5. Crie as tabelas do banco de dados com o código a seguir:</h3>

```bash
  python data/create_tables.py
```

<h3>6. Crie o usuário administrador para acessar o sistema, com o código a seguir:</h3>

```bash
  python data/create_user_admin.py
```

<h3>7. Rode o programa pelo arquivo main ou pelo seguinte código:</h3>

```bash
  python main.py
```
