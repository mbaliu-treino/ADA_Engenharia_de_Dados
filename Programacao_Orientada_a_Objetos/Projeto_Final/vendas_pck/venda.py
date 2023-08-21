from datetime import datetime
from medicamento_pkg import MedicamentoQuimio

class Vendas:
    desconto_idade = 0.2
    desconto_valor = 0.1

    def __init__(self, cliente):
        self.hora = datetime.now()
        self.cliente = cliente
        self._lista_de_produtos = []

    def adicionar_produto(self, *produtos_vendidos):
        """ Adiciona um produto à lista de vendas. 
        
        Verifica se algum produto é de venda controlada. Caso não seja confirmada 
        o recebimento de receita o produto não é adicionado.
        """

        for mdcmt in produtos_vendidos:
            # Verifica a restrição
            if isinstance(mdcmt, MedicamentoQuimio):
                if mdcmt.req_receita == True:
                    # Solicita a receita
                    print('---- ATENÇÃO ----\nProduto com venda controlada!\n')
                    receita_input = input(f'O cliente forneceu receita para o medicamento {mdcmt.nome}? (Y, N)')
                    if receita_input in ('Y', 'y'):
                        print('Produto incluído.')
                        self._lista_de_produtos.append(mdcmt)
                    else:
                        print('Produto não foi incluído na venda!')
            else:
                self._lista_de_produtos.append(mdcmt)
                

    @classmethod
    def desconto_total(self):
        """ Retorna o porcentual de desconto para o caso da venda. 

        Retorno
        -------
        Porcentual da venda : float
        """

        desconto = 0
        
        if (self.cliente.idade >= 65) and (desconto <= self.desconto_idade):
            desconto = self.desconto_idade
        
        if (self.valor_total >= 150) and (desconto <= self.desconto_valor):
            desconto = self.desconto_valor
        
        return desconto


    @property
    def valor_total(self):
        """ Calcula a soma final da operção de venda. """
        soma_produtos = 0
        for p in self._lista_de_produtos:
            soma_produtos += p.preco
        return soma_produtos
    
    @property
    def valor_total_final(self):
        """ Calcula o varlo final com desconto. """
        return self.valor_total * (1 - self.desconto_total)

# TESTE
# v = Vendas('Marcelo')
# v.adicionar_produto(1,1,1,1,1)
# print(v._lista_de_produtos)
# print(v.valor_total)