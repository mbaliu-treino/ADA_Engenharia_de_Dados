from cliente import CadastroClientes
from cliente import Cliente
from cliente import Cliente_Error, CPF_Error


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

        try:
            cliente_5 = Cliente('191', 'Marcelo', '01/05/1950')
            self.cadastro_clientes.adicionar_cliente(cliente_5)
        except Cliente_Error as e:
            print('ERRO: Cliente não adicionado! Não é possível usar o mesmo CPF.')
            print(f'[Cliente "{e.args[1].nome}:{e.args[1].cpf}" não pode sobrepor "{e.args[2].nome}:{e.args[2].cpf}"]')