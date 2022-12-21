from Estruturas.Arvore import AAVL
from Objetos.Ticket import Ticket
from Estruturas.Excecoes import CompraExcept
import random

class Vendas(object):
    def __init__(self):
        self.__arvore = AAVL()
    
    @property
    def arvore(self):
        return self.__arvore
    
    #Função que efetua a compra dentro da Arvore
    def comprar(self, nome, assento_escolhido, cidade_origem, cidade_destino, codigo_voo, voo_escolhido):
        id_compra = self.gerar_id_compra()
        while True:
            if self.arvore.busca(id_compra):
                id_compra = self.gerar_id_compra()
            else:
                break
        
        nova_compra = Ticket(id_compra, nome, assento_escolhido, cidade_origem, cidade_destino, codigo_voo, voo_escolhido)
        self.arvore.inserir(nova_compra)
        return id_compra
    
    #Função que retorna a compra efetuada de acordo com o ID da compra
    def verificar_compra(self, id_compra):
        try:
            compra_escolhida = self.arvore.dado_arvore(int(id_compra))
            dados_aviao =  list(compra_escolhida.dados.values())
            string_formatada = 'ID:{} | Nome: {} | Assento Comprado: {} |Origem -> {} | Destino -> {} '.format(dados_aviao[0], dados_aviao[1], dados_aviao[2], dados_aviao[3], dados_aviao[4])
            return string_formatada
        except:
            raise CompraExcept('Erro! Este ID é Inválido!!!')

    #Função que retorna todas as compras armazenadas na Arvore
    def compras_realizadas(self):
        vendas = ''
        dados = self.arvore.em_ordem()
        for i in dados:
            vendas += f' | {i} | '
        if vendas =='':
            vendas = 'Não existe ainda compras realizadas!'
        return vendas
    

    #Função que gera aleatoriamente um ID de compra
    def gerar_id_compra(self):
        id_compra = random.randint(10, 100)
        return id_compra
    

    #Função que cria um recibo
    def criar_recibo(self, id_compra):
        if self.arvore.busca(id_compra) == False:
            raise CompraExcept('Dado não existe')
        else:
            compra_escolhida = self.arvore.dado_arvore(int(id_compra))
            dados =  list(compra_escolhida.dados.values())
            nome_arquivo = f'Passagem Final ID {dados[0]}'
            arquivo = open(nome_arquivo, 'w+')
            arquivo.writelines(f''' 
                    +-------------------------------------+
                    |                                     |
                    |          CARTAO DE EMBARQUE         |
                    |                                     |
                    |          Data: 30/11/2022           |
                    |     Horario de embarque: 13:30      |
                    |               {dados[3]} -> {dados[4]}                |
                    |    Numero Companhia (619) 284-5142  |
                    |                                     |
                    |         ASSENTO COMPRADO:{dados[2]}          |
                    |                                     |
                    |  Subtotal                  399.99   |
                    |                                     |
                    |                                     |
                    |      NUMERO DO VOO: {dados[0]}              |
                    |      CODIGO DO VOO: {dados[5]}              |
                    |      CODIGO DO AVIÃO: {dados[6].upper()}           |
                    |                                     |
                    +-------------------------------------+''')
            arquivo.close()
            return nome_arquivo