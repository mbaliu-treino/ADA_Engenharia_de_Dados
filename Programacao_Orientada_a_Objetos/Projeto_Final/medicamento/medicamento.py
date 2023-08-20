

class Medicamento:
    # Cria a instância do cadastro de medicamentos
    # cadastro_medicamento = CadastroMedicamentos()

    def __init__(self, nome: str, composto_principal: str, laboratorio: str, descricao: str, preco: float):
        self.nome: str = nome
        self.composto_principal: str = composto_principal
        self.laboratorio: str = laboratorio
        self.descricao: str = descricao
        self.preco: float = preco

        # Adiciona no cadastro
        # self.cadastro_medicamento.adicionar_medicamento( self )


class MedicamentoFito(Medicamento):
    def __init__(self, nome: str, composto_principal: str, laboratorio: str, descricao: str, preco: float):
        super().__init__(nome, composto_principal, laboratorio, descricao, float(preco))


class MedicamentoQuimio(MedicamentoFito):
    def __init__(self, nome: str, composto_principal: str, laboratorio: str, descricao: str, preco: [float, int], req_receita: str = True):
        super().__init__(nome, composto_principal, laboratorio, descricao, float(preco))
        self.req_receita = req_receita