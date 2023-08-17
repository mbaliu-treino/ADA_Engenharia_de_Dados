# PROGRAMA DE E-COMMERCE DE FARMÁCIA
import sef_layouts


def mostrar_menu():
    # Exibe layout predefinido do menu
    layout_menu = sef_layouts.menu()
    print(layout_menu)



if __name__ == '__main__':
    """ Execução do sistema de e-commerce. """
    print('======== SISTEMA DE E-COMMERCE DE FARMÁRCIA ========')
    
    # MENU
    mostrar_menu()
    while True:

        entrada_user = input('\n1Insira o número da operação desejada: ')

        if entrada_user == '1':
            # Venda
            print('1 - Realizar venda')
            pass
        elif entrada_user == '2':
            # Consulta de medicamento
            print('1 - Realizar venda')
            pass
        elif entrada_user == '3':
            # Consulta de cliente
            print('3 - Buscar cliente por CPF')
            pass
        elif entrada_user == '4':
            # Relatório das vendas
            print('4 - Gerar relatório das vendas')
            pass
        elif entrada_user == '5':
            # Sair da execução
            print('5 - Sair')
            break
        else:
            # Entrada errada
            print('Nenhuma opção identificada. Tente novamente.')

    # Finalização da aplicação
    print('\nSalvando sistema de vendas...')
    print('Sistema finalizado. Até em breve!')