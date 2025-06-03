class Pedido:
    def __init__(self, valor_total, status, id=None):
        self._id = id
        self._valor_total = valor_total
        self._status = status
        