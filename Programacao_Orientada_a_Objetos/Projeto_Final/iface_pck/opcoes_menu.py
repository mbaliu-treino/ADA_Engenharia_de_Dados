import sef_layouts
from sis

from time import sleep

class OpcoesMenu:
    def __init__(self):
        pass

    @staticmethod
    def opcao_2_busca_medicamento():
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