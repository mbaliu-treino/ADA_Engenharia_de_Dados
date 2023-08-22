
def teste_venda():
    import sistema_farmacia
    from cliente_pkg import Cliente
    from vendas_pck.venda import Vendas

    sistema = sistema_farmacia.Farmacia()
    cliente_1 = Cliente('191', 'Joao Carlos', '01/05/1950')
    v = Vendas(cliente_1)
