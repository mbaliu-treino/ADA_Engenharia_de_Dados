# PROGRAMA DE E-COMMERCE DE FARMÁCIA
from typing import Optional
import sistema_farmacia
import sef_layouts
from time import sleep

from cliente import CadastroClientes
from cliente import Cliente
from iface_pck.opcoes_menu import OpcoesMenu



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

        # opcao = input('\nInsira o número da operação desejada: ')
        opcao = '2' #DEBUG

        if opcao == '1':
            # Venda
            OpcoesMenu.opcao_1_processo_venda(sistema)
            print('Retornando ao menu inicial\n')
            continue

        elif opcao == '2':
            # Consulta de medicamento
            OpcoesMenu.opcao_2_busca_medicamento(sistema)
            print('Retornando ao menu inicial\n')
            continue

        elif opcao == '3':
            # Consulta de cliente
            OpcoesMenu.opcao_3_busca_cliente(sistema)
            print('Retornando ao menu inicial\n')
            continue

        elif opcao == '4':
            # Relatório das vendas
            OpcoesMenu.opcao_4_relatorio_vendas(sistema)
            print('Retornando ao menu inicial\n')
            continue

        elif opcao == '5':
            # Sair da execução
            print('5 - Sair')
            sleep(1)
            break
        else:
            # Entrada errada
            print('Nenhuma opção identificada. Tente novamente.')

    # Finalização da aplicação
    print('\nSalvando sistema de vendas...')
    sleep(1)
    print('Sistema finalizado. Até em breve!')
    