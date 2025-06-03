class Produto:
  def __init__(self, nome, valor, id_categoria, descricao, disponibilidade, id=None):
    self._id = id
    self.nome = nome
    self.valor = valor
    self.id_categoria = id_categoria
    self.descricao = descricao
    self.disponibilidade = disponibilidade
