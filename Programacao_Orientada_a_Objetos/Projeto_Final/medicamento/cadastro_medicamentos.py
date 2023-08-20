from __future__ import annotations
from typing import List, Optional, TypeVar
Medicamento_obj = TypeVar('Medicamento_obj')

class CadastroMedicamentos:
    def __init__(self):
        self.__cadastro_medicamentos = []

    def adicionar_medicamento(self, obj_medicamento: Medicamento_obj) -> None:
        """ Adiciona um objeto Medicamento ao banco de cadastros. """
        self.__cadastro_medicamentos.append( obj_medicamento )

    def mostrar_medicamentos(self) -> List[Medicamento_obj]:
        """ Retorna todos medicamentos do cadastro. """
        return [medicamento for medicamento in self.__cadastro_medicamentos]

    def buscar_medicamento_por_nome(self, nome: str) -> Optional[Medicamento_obj]:
        """ Retorna o objeto de medicamento do nome buscado. 
        Caso nenhum medicamento seja encontrado será retornado None.

        Parâmetros
        ----------
            nome : str
                Nome a ser buscado no cadastro de medicamentos.

        Retorno
        -------
            medicamento(obj)
                - None caso não encontre nenhum medicamento com o nome.
        """

        if nome in self.__cadastro_medicamentos.keys():
            return self.__cadastro_medicamentos[nome]
        else:
            return None