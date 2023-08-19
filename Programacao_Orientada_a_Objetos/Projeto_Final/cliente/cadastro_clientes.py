#TODO>>> Proteger a edição dos objetos dentro do dicionário

from __future__ import annotations
from typing import List, Optional, TypeVar
Cliente = TypeVar('Cliente')
# from cliente import Cliente  #TODO >> remover 


class CadastroClientes:
    def __init__(self):
        self.__cadastro_clientes = {}

    ## @property
    # def _cadastro_clientes(self):
    #     """Método Property: mostra o cadastro. É uma operação técnica, logo ela é protegida."""
    #     return self.__cadastro_clientes.copy()  # COPY para evitar de alterar a estrutura do banco de dados
    
    def adicionar_cliente(self, obj_cliente: Cliente) -> None:
        """ Adiciona um objeto cliente ao banco de cadastros (__cadastro_clientes: Lista). """
        self.__cadastro_clientes[obj_cliente.cpf] = obj_cliente

    def mostrar_clientes(self) -> List['Cliente']:  
        """ Retorna todos clientes do cadastro. """
        return [cliente for cliente in self.__cadastro_clientes]

    def buscar_cliente_por_cpf(self, cpf: str) -> Optional['Cliente']:  
        """ Retorna o objeto de Cliente do CPF buscado. Caso nenhum cliente seja encontrado
        Será retornado None.

        Parâmetros
        ----------
            cpf : str
                CPF a ser buscado no cadastro de usuários.

        Retorno
        -------
            Cliente(obj)
                None caso não encontre nenhum clinte com o CPF.
        """

        if cpf in self.__cadastro_clientes.keys():
            return self.__cadastro_clientes[cpf]
        else:
            return None
        


