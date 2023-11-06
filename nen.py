from hatsu import *

class Nen(Hatsu):

  def __init__(self) -> None:
      self.__is_awakening: bool = False
      self.__ten: int = 0
      self.__zetsu: int = 0
      self.__ren: int = 0
      self._chance: int = 0
      
  def is_awake(self):
    return self.__is_awakening

  def _nen_baptism(self) -> None:
      if not self.__is_awakening:
          self.__is_awakening = True
          print('Seu batismo funcionou, agora pode usar nen!')
          super().__init__()
      else: print('Já está batizado!')

  def _nen_train_awake(self) -> None:
      if not self.__is_awakening and randint(self._get_chance(), 100) == 100:
          self.__is_awakening = True
          super().__init__()
          print('Seu treino funcionou, agora pode usar seu nen!')
      else: 
          print("Seu treino nao funcionou, continue treinando nen!")
  
  def _get_chance(self) -> int:
    self._chance = (self.get_ten() + self.get_ren() + self.get_zetsu())//3
    return self._chance

  def get_ten(self) -> int:
    return self.__ten

  def get_zetsu(self) -> int:
    return self.__zetsu

  def get_ren(self) -> int:
    return self.__ren

  def get_nen_percents(self) -> None:
    if self.__is_awakening:
      for x in self._types:
        print(f'{x} - {x.get_percent()}')

  def _nen_train_zetsu(self) -> None:
    if self.get_zetsu() < 100:
      self.__zetsu += 2
    else: print('Seu treino falhou')

  def _nen_train_ten(self) -> None:
    if self.get_ten() < 100:
      self.__ten += 2
    else: print('Seu treino falhou')

  def _nen_train_ren(self) -> None:
    if self.get_ren() < 100:
      self.__ren += 2
    else: print('Seu treino falhou')
