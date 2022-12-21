import random
from Estruturas.Fila import Fila
from Estruturas.Fila import Aviao
from Estruturas.Excecoes import AviaoException
#Classe aeroporto para tratar dados e armazenar métodos --> Para não criar as estruturas principais sem possibilidade de reutilização
#Recebe uma fila
class Aeroporto:
    def __init__(self):
        self.__fila = Fila()
#Encapsulamento da fila   
    @property
    def fila(self):
        return self.__fila
#Insere aviões na fila do aeroporto com informações de ID ,Origem, destino, assentos.
    def inserir_avioes(self):
        if self.fila.fila_cheia():
            raise AviaoException('Aeroporto com capacidade maxima! Não é possivel inserir!')
        dados = self.gerar_locais()
        aviao = Aviao(dados)
        aviao.preenche_assentos()
        self.fila.enfileira(aviao)
        if not self.fila.fila_cheia():
            return self.inserir_avioes()
#Remove Aviões da lista
    def remover_avioes(self):
        self.fila.desenfileira()
#Função para tratamento/compra que recebe a função "escolhe_assento" do avião   
    def comprar_cadeira(self, id_voo:str, cadeira:int):
        try:
            aviao_escolhido = self.fila.dado_fila(id_voo.strip())
            aviao_escolhido.escolhe_assento(cadeira)
        except AttributeError:
            raise AviaoException('Este ID não pertence a nenhum avião!')
#Função para Verificar cadeiras a partir do id do voo, pela função do avião "assentos_atuais"
    def verificar_cadeiras(self, id_voo:str):
        try:
            aviao_escolhido = self.fila.dado_fila(id_voo.strip())
            return aviao_escolhido.assentos_atuais()
        except AttributeError:
            raise AviaoException('Este ID não pertence a nenhum avião!')
#Função para retornar os dados do aviao em formato de lista, a partir de "info_aviao_cliente"
    def dados_aviao_id(self, id_voo):  
        try:
            aviao_escolhido = self.fila.dado_fila(id_voo.strip())
            dados_aviao = aviao_escolhido.info_aviao_cliente()
            return dados_aviao
        except AttributeError:
            raise AviaoException('Este ID não pertence a nenhum avião!')
#Inspeciona os dados do voo a partir do ID e retorna string formatada
    def inspecionar_dados_voo(self, id_voo:str):
        try:
            dados_aviao = self.fila.dado_fila(id_voo.strip())
            dados_aviao = dados_aviao.info_aviao_cliente()
            string_formatada = 'ID: {} | Origem -> {} | Destino -> {} '.format(dados_aviao[0], dados_aviao[1], dados_aviao[2])
        except AttributeError:
            raise AviaoException('Este ID não pertence a nenhum avião!')
        
        return string_formatada
#Gera o código do voo, constituido pela concatenação da sigla do estado de origem com o ID do avião e com a sigla do estado de destino
    def gerar_codigo(self, id_voo:str):
        try:
            dados = self.fila.dado_fila(id_voo.strip())
            array_dados = dados.info_aviao_cliente()
            inicio1_id = array_dados[1].split()
            inicio1_id = inicio1_id[-1:][-1:]
            fim1_id = array_dados[2].split()
            fim1_id = fim1_id[-1:][-1:]
            codigo_voo = f'{inicio1_id[0]}{array_dados[0]}{fim1_id[0]}'
            return codigo_voo
        except AttributeError:
            raise AviaoException('Este ID não pertence a nenhum avião!')
#Gera os locais de origem e destino para os aviões e retornam um list 
    def gerar_locais(self):
            locais = [
            "Rio Branco AC", "Macapá AP", "Manaus AM", "Belém PA", "Porto Velho RO",
                "Boa Vista RR", "Palmas TO", "Maceió Al", "Capital: Salvador BA",
                "Fortaleza CE", "São Luís MA", "João Pessoa PB", "Recife PE",
                "Teresina PI", "Natal RN", "Aracaju SE", "Goiânia GO", "Cuiabá MT",
                "Campo Grande MS", "Brasília DF", "Vitória ES", "Belo Horizonte MG",
                "São Paulo SP", "Rio de Janeiro RJ", "Curitiba PR", "Porto Alegre RS",
                "Florianópolis SC"
            ]
#Verificação para que origem e destino não sejam iguais.
            while True:
                locais_def = [random.choice(locais), random.choice(locais)]
                if locais_def[0] != locais_def[1]:
                    break
            return locais_def
#Método str
    def __str__(self):
        return f'{self.fila}'



