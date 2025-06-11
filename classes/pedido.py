class Pedido:
    def __init__(self, valor_total, status, id_metodo_pag, id_usuario, itens=None, id=None,):
        self._id = id
        self._valor_total = valor_total
        self._status = status
        self.itens = itens if itens else []
        self._id_metodo_pag = id_metodo_pag
        self._id_usuario = id_usuario
        