class Categoria:
  def __init__(self, nome, id=None):
    self._id = id
    self._nome = nome

  @property
  def id(self):
    return self._id
    
  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome