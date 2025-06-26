class Pedido:
    def __init__(self, data_hora, valor_total, status, id_metodo_pag, id_usuario, itens=None, id=None,  nome_usuario=None, nome_metodo_pagamento=None):
        self._id = id
        self._data_hora = data_hora
        self._valor_total = valor_total
        self._status = status
        self.itens = itens if itens else []
        self._id_metodo_pag = id_metodo_pag
        self._id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.nome_metodo_pagamento = nome_metodo_pagamento
        