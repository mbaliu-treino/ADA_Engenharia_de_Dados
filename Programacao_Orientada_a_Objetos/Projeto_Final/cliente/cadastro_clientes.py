#TODO>>> Proteger a edição dos objetos dentro do dicionário
from __future__ import annotations
from typing import List, Dict, Optional, TypeVar
Cliente_ = TypeVar('Cliente_')

from .c_exceptions import Cliente_Error



class CadastroClientes:
    """ 
    Descrição
    ---------
        O Cadastro de Clientes é estruturado em um dicionário com o CPF do cliente como chave.
        Isso melhora a performance da identificação dos clientes
    """

    def __init__(self):
        self.__cadastro_clientes: Dict = {}

    ## @property
    # def _cadastro_clientes(self):
    #     """Método Property: mostra o cadastro. É uma operação técnica, logo ela é protegida."""
    #     return self.__cadastro_clientes.copy()  # COPY para evitar de alterar a estrutura do banco de dados
    
    def adicionar_cliente(self, obj_cliente: Cliente_) -> None:
        """ Adiciona um objeto cliente ao banco de cadastros. """
        
        # Evita a sobreescrita de clientes já cadastrados
        if obj_cliente.cpf not in self.__cadastro_clientes.keys():
            self.__cadastro_clientes[obj_cliente.cpf] = obj_cliente
        else:
            obj_cliente_novo = obj_cliente
            obj_cliente_existente = self.__cadastro_clientes[obj_cliente.cpf]
            raise Cliente_Error(
                'CPF já cadastro.', 
                obj_cliente_novo, 
                obj_cliente_existente)

    def mostrar_clientes(self) -> List[Cliente_]:  
        """ Retorna todos clientes do cadastro. """
        return [cliente for cliente in self.__cadastro_clientes]

    def buscar_cliente_por_cpf(self, cpf: str) -> Optional[Cliente_]:  
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

        cpf_str = cpf.zfill(11)
        if cpf_str in self.__cadastro_clientes.keys():
            return self.__cadastro_clientes[cpf_str]
        else:
            return None
        


