from cliente_pkg import CadastroClientes
from cliente_pkg import Cliente
from cliente_pkg import Cliente_Error, CPF_Error

from medicamento_pkg import MedicamentoFito, MedicamentoQuimio
from medicamento_pkg import CadastroMedicamentos

from vendas_pck.cadastro_vendas import CadastroVendas

def print_log(*v, log=True):
    if log:
        print(*v)

class Farmacia:
    def __init__(self, preset=True, log=True):
        self.cadastro_clientes = CadastroClientes()
        self.cadastro_medicamentos = CadastroMedicamentos()
        self.cadastro_vendas = CadastroVendas()

        if preset:
            # CADASTRO DE CLIENTES DE TESTE
            if True:
                # [TODO >> pode ser alterado para um registro persistido em um arquivo]

                cliente_1 = Cliente('191', 'Joao Carlos', '01/05/1950')
                cliente_2 = Cliente('5'*11, 'Maria de Aparecida', '01/05/1950')
                cliente_3 = Cliente('6'*11, 'Pedro Souza', '01/12/2005')
                cliente_4 = Cliente('7'*11, 'Raquel Fiori', '19/08/2000')
                
                self.cadastro_clientes.adicionar_cliente(cliente_1)
                self.cadastro_clientes.adicionar_cliente(cliente_2)
                self.cadastro_clientes.adicionar_cliente(cliente_3)
                self.cadastro_clientes.adicionar_cliente(cliente_4)

                # try:
                #     cliente_5 = Cliente('191', 'Marcelo', '01/05/1950')
                #     self.cadastro_clientes.adicionar_cliente(cliente_5)
                # except Cliente_Error as e:
                #     print('>>> ERRO: Cliente não adicionado! Não é possível usar o mesmo CPF.')
                #     print(f'>>> [Cliente "{e.args[1].nome}:{e.args[1].cpf}" não pode sobrepor "{e.args[2].nome}:{e.args[2].cpf}"]')

            # CADASTRO DE MEDICAMENTOS TESTE
            if True:
                lista_medicamentos_fito = [
                    {'nome': 'remedio A', 'composto_principal': 'F1', 'laboratorio': 'L1', 'descricao': 'Medicamento para dores.', 'preco': 100.5},
                    {'nome': 'remedio B', 'composto_principal': 'F2', 'laboratorio': 'L2', 'descricao': 'Medicamento para dores.', 'preco': 150},
                    ]
                lista_medicamentos_quimio = [
                    {'nome': 'remedio Quimio A', 'composto_principal': 'Q1', 'laboratorio': 'L1', 'descricao': 'Medicamento para dores.', 'preco': 100.5, 'req_receita': False},
                    {'nome': 'remedio Quimio B', 'composto_principal': 'Q2', 'laboratorio': 'L3', 'descricao': 'Medicamento para dores.', 'preco': 300, 'req_receita': True},
                    ]
                

                mfA = MedicamentoFito(**lista_medicamentos_fito[0])
                mfB = MedicamentoFito(**lista_medicamentos_fito[1])
                print_log('>>> medicamentos criados', log=log)
                print_log('>>>', mfA.nome, mfA.composto_principal, mfA.descricao, mfA.laboratorio, log=log)
                self.cadastro_medicamentos.adicionar_medicamento(mfA)
                self.cadastro_medicamentos.adicionar_medicamento(mfB)
                print_log('>>> Medimaentos adicionados', log=log)

                mqA = MedicamentoQuimio(**lista_medicamentos_quimio[0])
                mqB = MedicamentoQuimio(**lista_medicamentos_quimio[1])
                print_log('>>> medicamentos criados', log=log)
                self.cadastro_medicamentos.adicionar_medicamento(mqA)
                self.cadastro_medicamentos.adicionar_medicamento(mqB)
                print_log('>>> Medimaentos adicionados', log=log)