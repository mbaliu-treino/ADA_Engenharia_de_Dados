
_iface_detalhes_mdcmt = """
• NOME DO MEDICAMENTO: {0},
• LABORATÓRIO: {1},
• TIPO DE MEDICAMENTO: {2}
• COMPOSTO PRINCIPAL: {3},
• PREÇO DO PRODUTO: R$ {4}
"""


class Medicamento:
    # Cria a instância do cadastro de medicamentos
    # cadastro_medicamento = CadastroMedicamentos()

    def __init__(self, nome: str, composto_principal: str, laboratorio: str, descricao: str, preco: float):
        self.nome: str = nome
        self.composto_principal: str = composto_principal
        self.laboratorio: str = laboratorio
        self.descricao: str = descricao
        self.preco: float = preco



class MedicamentoFito(Medicamento):
    def __init__(self, nome: str, composto_principal: str, laboratorio: str, descricao: str, preco: float):
        super().__init__(nome, composto_principal, laboratorio, descricao, float(preco))

    @property
    def detalhes_str(self):
        tipo_mdcmt = 'Fitoterápico'
        return _iface_detalhes_mdcmt.format(
            self.nome,
            self.laboratorio,
            tipo_mdcmt,
            self.composto_principal,
            self.preco
        ) + '---- Venda liberada ----'


class MedicamentoQuimio(MedicamentoFito):
    def __init__(self, nome: str, composto_principal: str, laboratorio: str, descricao: str, preco: [float, int], req_receita: str = True):
        super().__init__(nome, composto_principal, laboratorio, descricao, float(preco))
        self.req_receita = req_receita
    
    @property
    def detalhes_str(self):
        tipo_mdcmt = 'Quimioterápico'
        if self.req_receita:
            receita_mdcmt_str = 'RECEITA: OBRIGATÓRIA\n---- VENDA CONTROLADA ----'
        else:
            receita_mdcmt_str = 'RECEITA: Dispensada\n---- Venda liberada ----'

        return _iface_detalhes_mdcmt.format(
            self.nome,
            self.laboratorio,
            tipo_mdcmt,
            self.composto_principal,
            self.preco
            ) + receita_mdcmt_str
