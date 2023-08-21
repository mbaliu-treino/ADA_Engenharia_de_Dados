# Sistema de E-Commerce de farmárcia (sef)
# Classes com os layouts para a UI

_layout_menu = """
Escolha a opção que deseja realizar:

    1 - Realizar venda.
    2 - Buscar medicamento.
    3 - Buscar cliente por CPF.
    4 - Gerar relatório das vendas. [NÃO IMPLEMENTADO]
    5 - Sair
"""

_layout_menu_buscaMdcmt = """
Como deseja buscar o medicamento?

    1 - Buscar por nome
    2 - Buscar por laboratório
    3 - Buscar por descrição
"""


class menu:
    """ Menu incial do programa. """
    def __init__(self):
        self._layout_menu = _layout_menu

    def __repr__(self) -> str:
        return self._layout_menu
    
    @staticmethod
    def mostrar_menu():
        print(_layout_menu)

    @staticmethod
    def mostrar_submenu_mdcmt():
        print(_layout_menu_buscaMdcmt)