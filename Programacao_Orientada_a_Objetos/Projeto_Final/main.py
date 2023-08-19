# PROGRAMA DE E-COMMERCE DE FARMÁCIA
import sistema_farmacia
import sef_layouts

from cliente import CadastroClientes
from cliente import Cliente




if __name__ == '__main__':
    # Execução do sistema de e-commerce.
    print('======== SISTEMA DE E-COMMERCE DE FARMÁRCIA ========')

    # Inicialização do sistema (cadastros)
    sistema = sistema_farmacia.Farmacia()
    print('(Sistema inicializado com sucesso)')
    


    while True:
        # MENU
        print('== MENU ==')
        print( sef_layouts.menu() )

        opcao = input('\nInsira o número da operação desejada: ')

        if opcao == '1':
            # Venda
            print('1 - Realizar venda')
            pass
        elif opcao == '2':
            # Consulta de medicamento
            print('1 - Realizar venda')
            pass
        elif opcao == '3':
            # Consulta de cliente
            print('3 - Buscar cliente por CPF')
            procurar_cpf = input('Digite o CPF do cliente desejado: ')

            # Busca do cliente
            obj_cliente = sistema.cadastro_clientes.buscar_cliente_por_cpf(procurar_cpf)

            # Validação
            if obj_cliente == None:
                print('CPF não encontrado!')
                #TODO -> Voltar ao menu
                #TODO -> Pedir outro CPF
            else:
                print(  f'\nDADOS DO CLIENTE\n--------------------\n'
                      + f'  Nome do cliente: {obj_cliente.nome},\n'
                      + f'  CPF: {obj_cliente.cpf},\n'
                      + f'  Idade: {obj_cliente.idade},\n'
                      + f'  Data de nascimento: {obj_cliente.data_nascimento}\n'
                      + f'  Histórico de compras:\n...\n...\n...')

                break
        elif opcao == '4':
            # Relatório das vendas
            print('4 - Gerar relatório das vendas')
            pass
        elif opcao == '5':
            # Sair da execução
            print('5 - Sair')
            break
        else:
            # Entrada errada
            print('Nenhuma opção identificada. Tente novamente.')

    # Finalização da aplicação
    print('\nSalvando sistema de vendas...')
    print('Sistema finalizado. Até em breve!')