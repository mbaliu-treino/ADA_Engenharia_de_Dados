# PROGRAMA DE E-COMMERCE DE FARMÁCIA
import sistema_farmacia
import sef_layouts

from cliente import CadastroClientes




if __name__ == '__main__':
    # Execução do sistema de e-commerce.
    print('======== SISTEMA DE E-COMMERCE DE FARMÁRCIA ========')

    # Inicialização do sistema (cadastros)
    sistema_farmacia = sistema_farmacia.Farmacia()
    print('(Sistema inicializado com sucesso)')
    

    # MENU
    print( sef_layouts.menu() )

    while True:

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

            resultado_da_busca = CadastroClientes.buscar_cliente_por_cpf(procurar_cpf)
            if resultado_da_busca == None:
                print('CPF não encontrado!')
                #TODO -> Voltar ao menu
                #TODO -> Pedir outro CPF
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