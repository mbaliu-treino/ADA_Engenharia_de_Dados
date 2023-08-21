# python -Bc "for p in __import__('pathlib').Path('.').rglob('*.py[co]') : p.unlink()"
# python -Bc "for p in __import__('pathlib').Path('.').rglob('__pycache__') : p.rmdir()"
# 

import sistema_farmacia
import sef_layouts
from time import sleep

from iface_pck.opcoes_menu import OpcoesMenu
from vendas_pck.venda import Vendas


sistema = sistema_farmacia.Farmacia()

v = Vendas()
