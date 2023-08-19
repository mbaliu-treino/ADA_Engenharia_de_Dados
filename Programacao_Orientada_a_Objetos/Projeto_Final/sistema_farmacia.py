from cliente import CadastroClientes
from cliente import Cliente

class Farmacia:
    def __init__(self):
        self.cadastro_clientes = CadastroClientes()
        self.cadastro_medicamentos = None
        self.cadastro_vendas = None

        # Cria um cadastro de experimentação
        # [TODO >> pode ser alterado para um registro persistido em um arquivo]

        cliente_1 = Cliente('191', 'Joao Carlos', '01/05/1950')
        cliente_2 = Cliente('5'*11, 'Maria de Aparecida', '01/05/1950')
        cliente_3 = Cliente('6'*11, 'Pedro Souza', '01/12/2005')
        cliente_4 = Cliente('7'*11, 'Raquel Fiori', '19/08/2000')

        self.cadastro_clientes.adicionar_cliente(cliente_1)
        self.cadastro_clientes.adicionar_cliente(cliente_2)
        self.cadastro_clientes.adicionar_cliente(cliente_3)
        self.cadastro_clientes.adicionar_cliente(cliente_4)



    @staticmethod
    def __teste_criar_usuarios():
        """ Cria um conjunto de usuários no Cadastro de Clientes para a testagem do programa. """
        pass
