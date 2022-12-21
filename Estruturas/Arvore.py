from Estruturas.Excecoes import CompraExcept
    
#Implementação da Árvore

#Classe nó --------------------------------------------------------
class No(object):
  def __init__(self, dado):
    self.__carga = dado
    self.__esq = None
    self.__dir = None
    self.__altura = 1

  #Definindo os dados como atributos privados
  @property
  def carga(self) -> object:
    return self.__carga

  @property
  def esq(self) -> object:
    return self.__esq

  @property
  def dir(self) -> object:
    return self.__dir

  @property
  def altura(self) -> int:
    return self.__altura

  @altura.setter
  def altura(self, nova_altura: int):
    self.__altura = nova_altura

  @dir.setter
  def dir(self, nova_dir: object):
    self.__dir = nova_dir

  @esq.setter
  def esq(self, nova_esq: object):
    self.__esq = nova_esq

  #Retorno dos dados para testes
  def __str__(self) -> str:
    return f'{self.carga}'


#Classe da arvore AAVL ---------------------------------------------------------------------

class AAVL(object):

  def __init__(self, dado: object = None):
    if dado is None:
      self.__raiz = None
    else:
      self.__raiz = self.inserir(dado)

  #Definindo a raiz como dado privado
  @property
  def raiz(self) -> object:
    return self.__raiz

  @raiz.setter
  def raiz(self, no):
    self.__raiz = no
   
  #Verificação se a árvore não possui nós
  def esta_vazia(self) -> bool:
    return self.__raiz == None

  #Inserção de dados / Verificação de repetição nas instâncias de id_compra gerados.
  def inserir(self, dado:object):
    #Verificação para averiguar se já existe um nó
    if (self.__raiz == None):
      self.__raiz = No(dado)
    else:  #adiciona nós depois de já inicializar a árvore, fazendo isso por meio da chamda da função recursiva __inserir
      self.__raiz = self.__inserir(self.__raiz, dado)

  #insere os dados e verifica para manter a árvore balanceada

  def __inserir(self,raiz:object, dado:object):
    #verifica se a raiz atual já possui um nó
    if not raiz:
      return No(dado)
    #verifica se o id atual é menor que a raiz, para assim poder realizar uma inserção a esquerda, ao mesmo tempo que chama recursivamente a função para assim poder colocar o dado na posição ideal
    elif dado.id < raiz.carga.id:
      raiz.esq = self.__inserir(raiz.esq, dado)
    else:  #caso não seja menor, ele será colocado em uma posição a direita enquanto chama a função recursivamente para colocar o dado na posição ideal.
      raiz.dir = self.__inserir(raiz.dir, dado)

    #alterando a altura da raiz atual
    raiz.altura = 1 + max(self.get_altura(raiz.esq), self.get_altura(raiz.dir))

    #salvando o valor do balanceamento da raiz atual, para logo assim realizar as rotações de balanceamento
    fator_balanceamento = self.get_balanceamento(raiz)

    #verificações para a chamada dos metodos de rotações
    if fator_balanceamento > 1 and dado.id < raiz.esq.carga.id:
      return self.__dir_rot(raiz)

    if fator_balanceamento < -1 and dado.id > raiz.dir.carga.id:
      return self.__esq_rot(raiz)

    if fator_balanceamento > 1 and dado.id > raiz.esq.carga.id:
      raiz.esq = self.__esq_rot(raiz.esq)
      return self.__dir_rot(raiz)

    if fator_balanceamento < -1 and dado.id < raiz.dir.carga.id:
      raiz.dir = self.__dir_rot(raiz.dir)
      return self.__esq_rot(raiz)

    return raiz

  #Método de rotação a esquerda
  def __esq_rot(self, no: No) -> object:
    u = no.dir
    lado_rot = u.esq

    u.esq = no
    no.dir = lado_rot

    no.altura = 1 + max(self.get_altura(no.esq), self.get_altura(no.dir))
    u.altura = 1 + max(self.get_altura(u.esq), self.get_altura(u.dir))

    return u

  #Método de rotação a direita
  def __dir_rot(self, no: No) -> object:
    u = no.esq
    lado_rot = u.dir

    u.dir = no
    no.esq = lado_rot

    no.altura = 1 + max(self.get_altura(no.esq), self.get_altura(no.dir))
    u.altura = 1 + max(self.get_altura(u.esq), self.get_altura(u.dir))

    return u

  #Método que retorna a altura do nó escolhido
  def get_altura(self, no: No) -> int:
    if no is None:
      return 0
    return no.altura

  #Mé que calcula o balanceamento do nó escolhido
  def get_balanceamento(self, no: No) -> int:
    if not no:
      return 0

    return self.get_altura(no.esq) - self.get_altura(no.dir)

  #Método de percorrer a árvore em ordem, chamando a função recursiva __em_ordem
  def em_ordem(self):
    array = []
    self.__em_ordem(self.__raiz, array)
    return array

  #Método de percorrer em ordem
  def __em_ordem(self, no, array):
    if not no:
      return
    self.__em_ordem(no.esq, array)
    array.append(no.carga.id)
    self.__em_ordem(no.dir, array)

  #Método para deletar um nó, mantendo sempre o balanceamento 
  def delete(self, chave:object):
    if(self.raiz is not None):
      self.raiz = self.__delete(self.raiz, chave)
  
  def __delete(self, no, chave):
    if not no:
      return no
    elif chave<no.carga.id:
      no.esq = self.__delete(no.esq, chave)
    elif chave>no.carga.id:
      no.dir = self.__delete(no.dir, chave)
    else:
      if no.esq is None:
        temp = no.dir
        no = None
        return temp
      elif no.dir is None:
        temp = no.esq
        no = None
        return temp
      
      temp = self.get_menor_valor_no(no.dir)
      no = temp
      no.dir = self.__delete(no.dir, temp.carga)
    
    if no is None:
      return no
    
    no.altura = 1+max(self.get_altura(no.esq), self.get_altura(no.dir))
    balanceamento = self.get_balanceamento(no)

    if balanceamento > 1 and self.get_balanceamento(no.esq) >=0:
      return self.__dir_rot(no)
    
    if balanceamento < -1 and self.get_balanceamento(no.dir) <=0:
      return self.__esq_rot(no)
    
    if balanceamento > 1 and self.get_balanceamento(no.esq)<0:
      no.esq = self.__esq_rot(no.esq)
      return self.__dir_rot(no)
    
    if balanceamento < -1 and self.get_balanceamento(no.dir)>0:
      no.dir = self.__dir_rot(no.dir)
      return self.__esq_rot(no)

    return no
  
  def get_menor_valor_no(self, no):
    if no is None or no.esq is None:
      return no
    
    return self.get_menor_valor_no(no.esq)

  #Método de busca de um nó apatir de um id escolhido, chamando a função recursiva __busca
  def busca(self, id: int) -> any:
    return self.__busca(id, self.__raiz)

  #Método de busca 
  def __busca(self, id, no: No) -> bool:
    try:
      if no is None:
        return False
      if (id == no.carga.id):
        return True
      elif (id < no.carga.id and no.esq != None):
        return self.__busca(id, no.esq)
      elif (id > no.carga.id and no.dir != None):
        return self.__busca(id, no.dir)
      else:
        return False
    except TypeError:
      raise CompraExcept('Tipo de dado Inválido!')
#Verificação para saber se o ID existe (Função privada recursiva)
  def dado_arvore(self, chave):
      if not self.busca(chave):
        raise CompraExcept('Este ID não existe!')
      return self.__dado_arvore(chave, self.__raiz)
  
  def __dado_arvore(self, chave, no:No) -> any:
    if no is None:
      raise CompraExcept('Este ID não existe')
    if (chave == no.carga.id):
      return no.carga
    elif (chave < no.carga.id and no.esq != None):
      return self.__dado_arvore(chave, no.esq)
    elif (chave > no.carga.id and no.dir != None):
      return self.__dado_arvore(chave, no.dir)
    else:
      raise CompraExcept('Esta compra não existe')
