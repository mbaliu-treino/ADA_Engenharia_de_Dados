# Sistema de E-Commerce de farmárcia (sef)
# Classes com os layouts para a UI

_layout_menu = """
Escolha a opção que deseja realizar:

    1 - Realizar venda.
    2 - Buscar medicamento.
    3 - Buscar cliente por CPF.
    4 - Gerar relatório das vendas.
"""

class menu:
    def __init__(self):
        self._layout_menu = _layout_menu

    def __repr__(self) -> str:
        return self._layout_menu