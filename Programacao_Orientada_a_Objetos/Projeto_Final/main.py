# PROGRAMA DE E-COMMERCE DE FARMÁCIA
from typing import Optional
import sistema_farmacia
import sef_layouts
from time import sleep

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

        # opcao = input('\nInsira o número da operação desejada: ')
        opcao = '2' #DEBUG

        if opcao == '1':
            # Venda
            print('1 - Realizar venda')
            pass
        elif opcao == '2':
            # Consulta de medicamento
            print('2 - Buscar medicamento')
            sef_layouts.menu.mostrar_submenu_mdcmt()
            opcao_sub = input('Digite a opção desejada: ')
            
            if opcao_sub == '1':
                # Buscar por nome
                nome_mdcmt = input('Digite o nome do medicamento: ')
                mdcmt = sistema.cadastro_medicamentos.buscar_medicamento_por_nome(nome_mdcmt)
                if mdcmt == None:
                    print('Nenhum medicamento encontrado com este nome.')
                else:
                    print(mdcmt.detalhes_str)
                sleep(1)
            elif opcao_sub == '2':
                # Buscar por laboratório
                lab_nome = input('Digite o nome do laboratório: ')
                mdcmt_lista = sistema.cadastro_medicamentos.buscar_medicamento_por_laboratorio(lab_nome)

                # Menu para escolher o remédio
                if len(mdcmt_lista) == 0:
                    print('Nenhum medicamento deste laboratório foi encontrado.')
                else:
                    print('Os seguintes remédios foram encontrados:')
                    for idx, mdcmt in enumerate(mdcmt_lista):
                        print(f'  {idx+1} - {mdcmt.nome}')

                    opcao_mdcmt = input('Selecione o número do medicamento: ')

            elif opcao_sub == '3':
                # Buscar por tipo
                pass
            else:
                print('Opção inválida.')
            

            break #DEBUG
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