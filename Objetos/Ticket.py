#Classe dados de compra (Ticket)---------------------------------------

class Ticket(object):
  def __init__(self, id_compra, nome, cadeira, local_origem, local_destino, cod_voo='', id_aviao=''):
    self.__dados_ticket = dict(id=id_compra, comprador=nome, assento=cadeira, origem=local_origem, destino=local_destino, codigo=cod_voo, aviao=id_aviao)

#Definindo os dados como atributos privados
  @property
  def id(self) -> int:
    return self.__dados_ticket['id']

  @property
  def dados(self) -> dict:
    return self.__dados_ticket

  def dados_formatados(self):
    dados = list(self.dados.values())
    return dados

  def __eq__(self, dado: int) -> bool:
        return self.id == dado

  def __ne__(self, dado: int) -> bool:
        return self.id != dado

  def __gt__(self, dado: int) -> bool:
        return self.id > dado

  def __lt__(self, dado: int) -> bool:
        return self.id < dado

  #Retorno dos dados para testes
  def __str__(self) -> str:
    return f'{self.__dados_ticket}'
