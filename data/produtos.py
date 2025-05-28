from classes.produto import Produto

produtos = []

produto_teste = Produto(
  nome='Petit Gateau',
  valor=15.50,
  categoria='Sobremesas',
  descricao='teste produto',
  disponibilidade=True
)

produtos.append(produto_teste)