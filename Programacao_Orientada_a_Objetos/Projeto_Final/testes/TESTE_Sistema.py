
def teste_farma():
    import sistema_farmacia

    sistema = sistema_farmacia.Farmacia()

    print(sistema.cadastro_medicamentos.mostrar_medicamentos())
    print(sistema.cadastro_medicamentos.buscar_medicamento_por_nome('remedio Quimio A'))
    print(sistema.cadastro_medicamentos.buscar_medicamento_por_laboratorio('L1'))
    print(sistema.cadastro_medicamentos.buscar_medicamento_por_tipo('q'))