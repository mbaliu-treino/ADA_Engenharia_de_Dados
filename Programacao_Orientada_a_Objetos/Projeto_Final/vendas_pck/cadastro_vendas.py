from __future__ import annotations
from typing import List, Optional, TypeVar
Vendas_obj = TypeVar('Vendas_obj')


class CadastroVendas:
    def __init__(self):
        self.__cadastro_vendas = []

    def mostrar_vendas(self) -> List[Vendas_obj]:
        """ Retorna todos vendas do cadastro. """
        return [venda for venda in self.__cadastro_vendas]

    def adicionar_venda(self, obj_venda: Vendas_obj) -> None:
        """ Adiciona um objeto venda ao banco de cadastros. """
        self.__cadastro_vendas.append( obj_venda )
        