class Produto:
  def __init__(self, nome, valor, categoria, descricao, disponibilidade):
    self.nome = nome
    self.valor = valor
    self.categoria = categoria
    self.descricao = descricao
    self.disponibilidade = disponibilidade
    
  def ver_dados(self):
    print('\n----- Dados do produto -----')
    print(f'\Produto: {self.nome} - R$ {self.valor} \nCategoria: {self.categoria} \nDescrição: {self.descricao} \nDisponível: {'Sim' if self.disponibilidade else 'Não'}')
