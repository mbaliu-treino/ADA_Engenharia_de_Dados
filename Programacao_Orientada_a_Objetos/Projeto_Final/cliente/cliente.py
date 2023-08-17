# entidades.py
from __future__ import annotations
from datetime import datetime, date
from typing import List

import cadastro_clientes


# ERROR CLASS
class CPF_Error(Exception):
    pass


# CLASSES
class Cliente:
    cadastro_obj = cadastro_clientes.CadastroClientes()

    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        """ARGS
            data_nascimento: str ('01/01/1990')
        """
        # Valida o CPF
        cpf_str = cpf.zfill(11)
        if self.cpf_valido(cpf_str):
            self.__cpf: str = cpf_str
        else:
            raise CPF_Error(f'O CPF inserido ({cpf_str}) é inválido! CPF não existente.')

        self.nome: str = nome
        self.__data_nascimento: date = self.casting_data_nascimento( data_nascimento )
        self.__historico_compras: List = []

        self.cadastro_obj.adicionar_cliente(self)  # <<<


    @property
    def idade(self) -> int:
        """Retorna o cálculo da idade."""
        hoje = datetime.today()
        idade = hoje.year - self.data_nascimento.year
        # Correção do mês
        # if
        return idade

    @staticmethod
    def verificar_cv_cpf(cpf_str: str):
        # Obtém os número em Integer
        numeros = [int(numero) for numero in cpf_str]

        # Validação do primeiro dígito verificador
        soma_dos_produtos = sum( a*b for a, b in zip(numeros[0:9], range(10, 1, -1)) )
        CV_1o = (soma_dos_produtos * 10 % 11) % 10
        if numeros[9] != CV_1o:
            return False

        # Validação do segundo dígito verificador
        soma_dos_produtos = sum(a*b for a, b in zip(numeros[0:10], range(11, 1, -1)))
        CV_2o = (soma_dos_produtos * 10 % 11) % 10
        if numeros[10] != CV_2o:
            return False
        return True

    @classmethod
    def cpf_valido(cls, cpf_str: str) -> bool:
        """Validar de CPF. Verifica o tamnho e o sufixo de verificação."""

        if len(cpf_str) != 11:
            # raise CPF_Error('O CPF inserido é inválido! Número de digitos incompatível.')
            return False
        elif not cls.verificar_cv_cpf(cpf_str):
            return False
        else:
            return True


    @classmethod
    def casting_data_nascimento(cls, data_nascimento_str: str) -> date:
        """Transforma o string da data de nascimento."""
        if '/' in data_nascimento_str:
            return datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
        else:
            return date.fromisoformat(data_nascimento_str)


    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento


    @property
    def historico_compras(self) -> List[Venda]:
        return self.__historico_compras

    def ADD_compra(self, operacao_de_venda: Venda) -> None:
        self.__historico_compras.append(operacao_de_venda)


