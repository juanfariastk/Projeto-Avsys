from Objetos.Aviao import *
from Estruturas.Excecoes import AviaoException, CompraExcept



#Implementação da fila---------------------------------------

#Nó cabeça da fila
class No_cabeca:

  def __init__(self):
    self.__inicio = None
    self.__final = None
    self.__tamanho = 0

#Definindo dados como atributos privados
  @property
  def inicio(self):
    return self.__inicio

  @property
  def final(self):
    return self.__final

  @property
  def tamanho(self):
    return self.__tamanho

  @tamanho.setter
  def tamanho(self, tamanho_novo):
    self.__tamanho = tamanho_novo

  @final.setter
  def final(self, final_atual):
    self.__final = final_atual

  @inicio.setter
  def inicio(self, inicio_atual):
    self.__inicio = inicio_atual

#Nó da fila--------------------------------------------------
class No1:

  def __init__(self, dado:object):
    self.__carga = dado
    self.__prox = None

  #Definindo dados como atributos privados
  @property
  def carga(self):
    return self.__carga

  @property 
  def prox(self):
    return self.__prox
  
  @prox.setter
  def prox(self, novo_prox):
    self.__prox = novo_prox

  def __str__(self):
    dados = ''
    dados += f'{self.carga} {self.prox}'
    return dados


#Início da fila
class Fila:

  def __init__(self):
    self.__cabeca = No_cabeca()

  @property
  def cabeca(self):
    return self.__cabeca

  def fila_cheia(self) -> bool:
    return self.cabeca.tamanho == 5

  def esta_vazia(self) -> bool:
    return self.cabeca.tamanho == 0

  def tamanho(self) -> int:
    return self.cabeca.tamanho

  def __len__(self) -> int:
    return self.cabeca.tamanho

  def elemento(self, posicao: int) -> any:
    try:
      assert posicao > 0 and posicao <= self.cabeca.tamanho

      apontador = self.cabeca.inicio
      count = 1
      while (count < posicao):
        apontador = apontador.prox
        count += 1
      return apontador.carga
    except AssertionError:
      raise AviaoException(f'Erro! Posicao inválida para a fila atual com elementos')

#Função que enfileira
  def enfileira(self, dado):
    if self.fila_cheia():
      raise AviaoException('Fila Cheia')

    novo = No1(dado)
    if self.esta_vazia():
      self.cabeca.inicio = novo
      self.cabeca.final = novo
    else:
      self.cabeca.final.prox = novo
      self.cabeca.final = novo
    self.cabeca.tamanho += 1

# Remove o dado
  def desenfileira(self) -> any:
    dado_removido = self.cabeca.inicio
    self.cabeca.inicio = self.cabeca.inicio.prox
    self.cabeca.tamanho -= 1
    return dado_removido

  def busca(self, chave: any) -> int:
    inicio = self.cabeca.inicio
    cont = 0
    while(inicio):
      cont+=1
      if inicio.aviao_id == chave:
        return cont
      inicio = inicio.prox
    raise AviaoException(f'Erro: o {chave} não está na Fila.')

  def __str__(self):
    dados_str = ''
    inicio = self.cabeca.inicio
    while (inicio):
      dados_str += f' {inicio.carga.id} |'
      inicio = inicio.prox
    dados_str = dados_str[:-2]
    return dados_str

  def esvazia(self):
    while(not self.estaVazia()):
      self.desenfileira()
  
  def dado_fila(self, chave):
    try:
      inicio = self.cabeca.inicio
      while (inicio):
        if inicio.carga.id == chave.upper():
          return inicio.carga
        else:
          inicio = inicio.prox
    except:
      raise AviaoException('Chave inválida para a busca!')
  


