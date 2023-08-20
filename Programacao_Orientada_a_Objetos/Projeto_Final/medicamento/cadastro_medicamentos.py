from __future__ import annotations
from typing import List, Optional, TypeVar
Medicamento_obj = TypeVar('Medicamento_obj')

from .medicamento import MedicamentoFito, MedicamentoQuimio

class CadastroMedicamentos:
    def __init__(self):
        self.__cadastro_medicamentos = []

    def mostrar_medicamentos(self) -> List[Medicamento_obj]:
        """ Retorna todos medicamentos do cadastro. """
        return [medicamento for medicamento in self.__cadastro_medicamentos]

    def adicionar_medicamento(self, obj_medicamento: Medicamento_obj) -> None:
        """ Adiciona um objeto Medicamento ao banco de cadastros. """
        self.__cadastro_medicamentos.append( obj_medicamento )

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
        for mdcmt in self.__cadastro_medicamentos:
            if mdcmt.nome == nome:
                return mdcmt
            else:
                return None
        
    def buscar_medicamento_por_laboratorio(self, lab_nome: str) -> List[Medicamento_obj]:
        """ Retorna o objeto de medicamento do ____ buscado. 
        Caso nenhum medicamento seja encontrado será retornado None.

        Parâmetros
        ----------
            ____ : str
                ____ a ser buscado no cadastro de medicamentos.

        Retorno
        -------
            Lista com todos os medicamentos do laboraório
        """
        resultado = []
        for mdcmt in self.__cadastro_medicamentos:
            if mdcmt.laboratorio == lab_nome:
                resultado.append(mdcmt)
        return resultado
            
    def buscar_medicamento_por_tipo(self, tipo_medicamento: str) -> List[Medicamento_obj]:
        """ Retorna o objeto de medicamento do ____ buscado. 
        Caso nenhum medicamento seja encontrado será retornado None.

        Parâmetros
        ----------
            ____ : str
                ____ a ser buscado no cadastro de medicamentos.

        Retorno
        -------
            Lista com todos os medicamentos do mesmo tipo [fitoterápico ou quimioterápico]
        """
        if tipo_medicamento.upper() in ('Q', 'QUIMIO', 'QUIMIOTERAPICO'):
            tipo_buscado = MedicamentoQuimio
        elif tipo_medicamento.upper() in ('F', 'FITP', 'FITOTERAPICO'):
            tipo_buscado = MedicamentoFito

        resultado = []
        for mdcmt in self.__cadastro_medicamentos:
            if isinstance(mdcmt, tipo_buscado):
                resultado.append(mdcmt)
        return resultado
        