import sef_layouts
from vendas_pck.venda import Vendas
from cliente_pkg import Cliente
from cliente_pkg import Cliente_Error, CPF_Error
from medicamento_pkg import MedicamentoQuimio

from time import sleep

import sistema_farmacia  #DEBUGGER


class OpcoesMenu:
    def __init__(self):
        pass

    @staticmethod
    def manter_busca_continua():
        """ Função auxiliar de entrada de usuário para manter o loop """
        opcao_busca = input('Continuar pesquisa (1) ou voltar ao menu inicial (2)? ')
        if opcao_busca == '1':
            return True
        elif opcao_busca == '2':
            return False
        else:
            return True
        
    @staticmethod
    def manter_operacao_continua():
        """ Função auxiliar de entrada de usuário para manter o loop """
        opcao_operacao = input('Continuar operação (1) ou voltar ao menu inicial (2)? ')
        if opcao_operacao == '1':
            return True
        elif opcao_operacao == '2':
            return False
        else:
            return True
        

    @staticmethod
    def opcao_1_processo_venda(sistema):
        """ Implementa a interface de venda. 

        Argumentos
        ----------
        sistema : objeto Farmacia
            Instância do sistema de farmácia em utilização.
        """

        print('1 - Realizar venda')
        
        busca_continua = True
        while busca_continua:
            # Verificação de cadastro
            opcao_cliente = input('O cliente já tem cadastro? (Y ou N) ')
            if opcao_cliente in ('Y', 'y'):
                # Realização de venda

                # Seleção de cliente pelo CPF
                cpf_cliente = input('Digite o CPF do cliente: ')
                cliente_inst = sistema.cadastro_clientes.buscar_cliente_por_cpf(cpf_cliente)
                if cliente_inst is None:
                    print('Cliente não encontrado.\n')
                else:
                    print('Venda inicializada:')

                    # Operação de venda
                    v = Vendas(cliente_inst)

                    # Produtos
                    add_produto = True
                    while add_produto:
                        add_produto_input = input('Deseja adicionar um produto? (Y ou N) ')
                        
                        # Encerra as compras
                        if add_produto_input in ('N', 'n'):
                            break
                        
                        # Produtos disponíveis
                        print('\nQual produto deseja comprar?')
                        lista_produtos = sistema.cadastro_medicamentos.mostrar_medicamentos()
                        for idx, mdcmt in enumerate(lista_produtos):
                            print(f'  {idx+1}. {mdcmt.nome} - R$ {mdcmt.preco:.2f}.')
                        
                        escolha_user = int(input('Por favor, escolha o número do produto desejado: '))
                        if escolha_user in range(1, len(lista_produtos)+1):
                            mdcmt = lista_produtos[escolha_user-1]
                            v.adicionar_produto( mdcmt )
                        else:
                            print('Número não válido!')
                    
                    # Finalização das compras
                    print('Finalizando compras ...\n\nRECIBO DE VENDA')
                    print(f'O valor das compra é de R$ {v.valor_total:.2f}')
                    print(f'O cliente recebeu desconto de {v.desconto_total():.2%}\n')
                    print(f'Valor a ser pago: R$ {v.valor_total_final:.2f}\n')
                    

                    # Adição do registro de venda nos registros
                    sistema.cadastro_vendas.adicionar_venda( v )
                    cliente_inst.ADD_compra( v )

                    sleep(2)
                    print('Fim da compra!')
                    sleep(1)
                
            elif opcao_cliente in ('N', 'n'):
                # Verificação se continua cadastro
                opcao_venda = input('Deseja cadastrar um novo cliente ou cancelar a venda? (Y ou N) ')
                if opcao_venda in ('Y', 'y'):
                    # Cadastrar novo cliente
                    print('Cadastrar um novo cliente')
                    # Dados do usuário
                    cliente_nome = input('Qual o nome do cliente? ')
                    cliente_cpf = input('Qual o CPF do cliente? (sem pontos ou barra) ')
                    cliente_data_nasc = input('Qual a data de nascimento? (dd/mm/aaaa ou aaaa-mm-dd) ')

                    # Criação do uário
                    cliente_novo = Cliente(nome=cliente_nome, cpf=cliente_cpf, data_nascimento=cliente_data_nasc)
                    try:
                        sistema.cadastro_clientes.adicionar_cliente( cliente_novo )
                        print('Cliente criado!\n')
                    except Cliente_Error as e:
                        print('>>> ERRO: Cliente não adicionado! Não é possível usar o mesmo CPF.')
                        print(f'>>> [Cliente "{e.args[1].nome}:{e.args[1].cpf}" não pode sobrepor "{e.args[2].nome}:{e.args[2].cpf}"]\n')
                        sleep(1)

                elif opcao_cliente in ('N', 'n'):
                    print('\n')
                else:
                    print('Opção inválida\n')
            else:
                print('Opção inválida\n')

            busca_continua = OpcoesMenu.manter_operacao_continua()

        sleep(1)
        

    @staticmethod
    def opcao_2_busca_medicamento(sistema):
        """ Implementa a interface de busca por medicamentos. 

        Argumentos
        ----------
        sistema : objeto Farmacia
            Instância do sistema de farmácia em utilização.
        """

        # Display
        print('2 - Buscar medicamento')       
            
        busca_continua = True
        while busca_continua:
            sef_layouts.menu.mostrar_submenu_mdcmt()

            # SUBMENU
            opcao_sub = input('Digite a opção desejada: ')
            if opcao_sub == '1':
                # Buscar por nome
                nome_mdcmt = input('Digite o nome do medicamento: ')
                mdcmt = sistema.cadastro_medicamentos.buscar_medicamento_por_nome(nome_mdcmt)
                if mdcmt == None:
                    # Nenhum resultado
                    print('Nenhum medicamento encontrado com este nome.')
                else:
                    # Display dos dados do medicamento
                    print(mdcmt.detalhes_str)
                sleep(1)

                busca_continua = OpcoesMenu.manter_busca_continua()

            elif opcao_sub == '2':
                # Buscar por laboratório
                lab_nome = input('Digite o nome do laboratório: ')
                mdcmt_lista = sistema.cadastro_medicamentos.buscar_medicamento_por_laboratorio(lab_nome)

                if len(mdcmt_lista) == 0:
                    # Nenhum medicamento encontrado
                    print('Nenhum medicamento deste laboratório foi encontrado.')
                else:
                    # Menu para escolher o remédio
                    print('Os seguintes remédios foram encontrados:')
                    for idx, mdcmt in enumerate(mdcmt_lista):
                        # Display dos medicamentos encontrados
                        print(f'  {idx+1} - {mdcmt.nome}')

                    opcao_mdcmt = int( input('Selecione o número do medicamento: ') )

                    # Detalhes do medicamento
                    if opcao_mdcmt in range(1, len(mdcmt_lista)):
                        mdcmt = mdcmt_lista[ opcao_mdcmt-1 ]
                        print(mdcmt.detalhes_str, '\n')
                        sleep(1)

                    sleep(1)
                    busca_continua = OpcoesMenu.manter_busca_continua()
            
            elif opcao_sub == '3':
                # Buscar por tipo
                lab_nome = input('Digite o tipo de medimento (quimio ou fito; Q ou F): ')
                mdcmt_lista = sistema.cadastro_medicamentos.buscar_medicamento_por_tipo(lab_nome)

                # Menu para escolher o remédio
                if len(mdcmt_lista) == 0:
                    print('Nenhum medicamento deste tipo foi encontrado.')
                else:
                    print('Os seguintes remédios foram encontrados:')
                    for idx, mdcmt in enumerate(mdcmt_lista):
                        # Display dos medicamentos encontrados
                        print(f'  {idx+1} - {mdcmt.nome}')

                    opcao_mdcmt = input('Selecione o número do medicamento: ')
                    # Detalhes do medicamento

                    if opcao_mdcmt in range(1, len(mdcmt_lista)):
                        mdcmt = mdcmt_lista[ opcao_mdcmt-1 ]
                        print(mdcmt.detalhes_str, '\n')
                        sleep(1)

                    sleep(1)
                    busca_continua = OpcoesMenu.manter_busca_continua()
            else:
                print('Opção inválida.')
                sleep(1)
                busca_continua = OpcoesMenu.manter_busca_continua()
        

    @staticmethod
    def opcao_3_busca_cliente(sistema):
        """ Implementa a interface de busca de cliente. 

        Argumentos
        ----------
        sistema : objeto Farmacia
            Instância do sistema de farmácia em utilização.
        """

        # Consulta de cliente
        print('3 - Buscar cliente por CPF')

        busca_continua = True
        while busca_continua:
            procurar_cpf = input('Digite o CPF do cliente desejado: ')

            # Busca do cliente
            obj_cliente = sistema.cadastro_clientes.buscar_cliente_por_cpf(procurar_cpf)

            # Validação
            if obj_cliente == None:
                print('CPF não encontrado!')
            else:
                print(  f'\nDADOS DO CLIENTE\n--------------------\n'
                        + f'  Nome do cliente: {obj_cliente.nome},\n'
                        + f'  CPF: {obj_cliente.cpf},\n'
                        + f'  Idade: {obj_cliente.idade},\n'
                        + f'  Data de nascimento: {obj_cliente.data_nascimento}\n'
                        + f'  Histórico de compras:\n...\n...\n...')
            sleep(1)
            busca_continua = OpcoesMenu.manter_busca_continua()


    @staticmethod
    def opcao_4_relatorio_vendas(sistema):
        """ Implementa a interface de relatório de vendas. 

        Argumentos
        ----------
        sistema : objeto Farmacia
            Instância do sistema de farmácia em utilização.
        """

        # Relatório das vendas
        print('4 - Gerar relatório das vendas')

        # sistema = sistema_farmacia.Farmacia(preset=True, log=False)  #DEBUGGER
        # Medicamentos por ordem alfabetica
        sistema.cadastro_medicamentos.relatorio_ordem_alfabeta()
        sleep(1)
        pass
