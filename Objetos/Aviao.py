import string
import random
from Estruturas.Excecoes import AviaoException, CompraExcept

#classe avião------------------------------------------------
class Aviao(object):

  def __init__(self, locais_def:list):
    self.__letras = string.ascii_uppercase
    # ID para identificar propriamente o avião: O id do aviao será gerado assim que o nó for criado, não precisando setar ele ao criar o node.
    self.__id_aviao = f'{random.randint(101,333)}{random.choice(self.__letras)}{random.choice(self.__letras)}'
    #Origem e destino do avião, geradas por função gerar_locais
    self.__origem = locais_def[0]
    self.__destino = locais_def[1]
    #Assentos disponíveis, ocupados, e geração de matriz.
    self.__assentos = [[None] * 4 for i in range(2)]
    self.__assentos_ocupados = list()

#Definindo as propriedades do objeto como atributos privados

  @property
  def id(self):
    return self.__id_aviao

  @property
  def origem(self):
    return self.__origem

  @property
  def destino(self):
    return self.__destino

  @property
  def assentos(self):
    return self.__assentos

  @property
  def prox(self):
    return self.__prox

  @property
  def assentos_ocupados(self):
    return self.__assentos_ocupados

  @origem.setter
  def origem(self, nova_origem):
    self.__origem = nova_origem

  @destino.setter
  def destino(self, novo_destino):
    self.__destino = novo_destino

  @assentos.setter
  def assentos(self, pos1, pos2, marca):
    self.__assento[pos1][pos2] = marca

  @id.setter
  def id(self, novo_id):
    self.__id_aviao = novo_id

#Função que vai inserir os assentos que estão ocupados

  @assentos_ocupados.setter
  def assentos_ocupados(self, num):
    self.assentos_ocupados.append(num)

  def __eq__(self, dado: int) -> bool:
        return self.id == dado

  def __ne__(self, dado: int) -> bool:
        return self.id != dado

  def __gt__(self, dado: int) -> bool:
        return self.id > dado

  def __lt__(self, dado: int) -> bool:
        return self.id < dado

  #Preenche o objeto avião com os assentos
  
  def preenche_assentos(self):
    for i in range(2):
      for j in range(4):
        if i == 1:
          self.assentos[i][j] = j + 5
        else:
          self.assentos[i][j] = j + 1

#Função que verifica a disponibilidade de compra de um assento

  def verificar_disponibilidade(self, num):
    for i in range(len(self.assentos_ocupados)):
      if self.assentos_ocupados[i] == num:
        raise CompraExcept('ERROR: Assento já foi comprado!')

  #Função que vai definir o assento a ser comprado

  def escolhe_assento(self, num):
    self.verificar_disponibilidade(num)
    if num>8 or num<=0:
      raise AviaoException('Digite um assento valido!')
    for i in range(2):
      for j in range(4):
        if self.assentos[i][j] == num:
          self.assentos[i][j] = 'X'
          self.assentos_ocupados.append(num)
    print('Comprado com sucesso!')

  #Mostra no terminal os assentos
  def assentos_atuais(self) -> str:
    string_fim = ''
    for i in range(2):
        string_fim+='\n'
        for j in range(4):
            string_fim+=f' [{self.assentos[i][j]}] '
    string_fim+='\n'
    return string_fim

  #Retorna as informações disponíveis antes da compra ser efetuada em uma lista para "acoplar" nos aviões e em métodos posteriores.
  def info_aviao_cliente(self):
    info_pre_compra = list((self.id, self.origem, self.destino))
    return info_pre_compra

  #Função criada para gerar um novo ID, será utilizada caso a verificação de repetição seja true.
  def atualizar_id_aviao(self):
    self.id_aviao = f'{random.randint(101,333)}{random.choice(self.__letras)}{random.choice(self.__letras)}'

  def __str__(self) -> str:
    dados = f'{self.id} | {self.origem} {self.destino} | {self.assentos_ocupados} | {self.assentos}'
    return dados
