import cadastro_clientes
import cliente

# TESTE >> Cliente
# Criação de objeto
print('======== TESTE CRIAÇÃO DE OBJETO ========')
cA = cliente.Cliente('1'*11, 'Marcelo', '1/04/1990')
cB = cliente.Cliente('191', 'BB_pessoal', '1/04/1900')
cC = cliente.Cliente('2'*11, 'Rodrigo', '15/08/2000')
print(f'{cA=}')
print(f'{cA.idade=}')
print('======== Criação de objetos Cliente executado ========\n')

# TESTE >> CPF
print('======== TESTE DE CPF ========')

# Verificação de CPF criado
print(f'{cA.cpf=}')

# Setting do CPF
print("cA.cpf = '0'", '>>> AttributeError: cant set attribute cpf')
## >>> AttributeError: can't set attribute 'cpf'

# Entrada errada de CPF
try:
    cCPF_errado = cliente.Cliente('111', 'Marcelo', '1/04/1990')
    ## >>> CPF_Error: O CPF inserido é inválido! CPF inexistente.
except cliente.CPF_Error as e:
    print(e)
print('======== Funcionalidade (CPF) verificada ========\n')



# TESTE >> idade
print('\n======== TESTE DE IDADE ========')
print(f'{cA.data_nascimento=}')
# cliente.Cliente('1'*11, 'Marcelo', '1/04/19901')  # ValueError
print('======== Funcionalidade (idade) verificada ========\n')


# Teste de CadastroClientes
print('======== CADASTRO DE CLIENTES ========')
cadastro_teste = cadastro_clientes.CadastroClientes()
print('CADASTRO LÓGICO (somente a chave dos clientes):\n', cadastro_teste.mostrar_clientes())  # mostra somente a chave dos clientes

# # Adiciona cliente
cadastro_teste.adicionar_cliente(cA)
cadastro_teste.adicionar_cliente(cB)
cadastro_teste.adicionar_cliente(cC)
print('• Clientes adicionados •\n')

# # Mostra do cadastro
# print('CADASTRO BRUTO:\n',  cadastro_teste.__cadastro_clientes)
print('CADASTRO LÓGICO (somente a chave dos clientes):\n', cadastro_teste.mostrar_clientes())  # mostra somente a chave dos clientes
print('• Persistência de usuários •')
print('======== Funcionalidade (cadastro) verificada ========\n')

# # TESTE DE BUSCA DE CPF
print('======== TESTE DE BUSCA DE CPF ========')
# CPF não existente -> None
print(cadastro_teste.buscar_cliente_por_cpf('1'*8))
# CPF existente -> Cliente
print(cadastro_teste.buscar_cliente_por_cpf('1'*11))
print('======== Funcionalidade (busca de CPF) verificada ========\n')



# # Teste de CadastroClientes

# cadastro_teste = cadastro_clientes.CadastroClientes()
# # Adiciona cliente
# cadastro_teste.adicionar_cliente(cliente1)
# # Mostra do cadastro
# print(cadastro_teste._cadastro_clientes)

# # Altera cadastro
# """Com a função COPY, o dicionário não é mais editável"""
# cadastro_teste._cadastro_clientes['VIRUS'] = ''
# print(cadastro_teste._cadastro_clientes)


