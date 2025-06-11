class ItemPedido:
    def __init__(self, nome, observacoes, valor_unit, quantidade, id_pedido, id_produto):
        self._nome = nome
        self._observacoes = observacoes
        self._valor_unit = valor_unit
        self._quantidade = quantidade
        self._id_pedido = id_pedido
        self._id_produto = id_produto