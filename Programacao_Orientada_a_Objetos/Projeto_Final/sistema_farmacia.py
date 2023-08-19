from cliente import CadastroClientes

class Farmacia:
    def __init__(self):
        self.cadastro_clientes = CadastroClientes()
        self.cadastro_medicamentos = None
        self.cadastro_vendas = None