class item_pedido:
    def __init__(self, nome, observacoes, valor_unit, quantidade, id=None):
        self._id = id
        self._nome = nome
        self._observacoes = observacoes
        self._valor_unit = valor_unit
        self._quantidade = quantidade