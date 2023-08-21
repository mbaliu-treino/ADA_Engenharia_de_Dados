import sef_layouts

from time import sleep

class OpcoesMenu:
    def __init__(self):
        pass

    @staticmethod
    def opcao_1_processo_venda(sistema):
        """ Implementa a interface de venda. 

        Argumentos
        ----------
        sistema : objeto Farmacia
            Instância do sistema de farmácia em utilização.
        """

        print('1 - Realizar venda')
        sleep(1)
        pass

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

                opcao_mdcmt = input('Selecione o número do medicamento: ')
                sleep(1)
                pass #TODO
        
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
                    print(f'  {idx+1} - {mdcmt.nome}')

                opcao_mdcmt = input('Selecione o número do medicamento: ')
                sleep(1)
                pass
        else:
            print('Opção inválida.')
            sleep(1)
        
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
        sleep(1)

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
        sleep(1)
        pass
