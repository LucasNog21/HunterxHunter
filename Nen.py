from hatsu import *

class Nen(Hatsu):
  chance: int = 1

  def __init__(self) -> None:
      self.__is_awakening: bool = False
      self.__ten: int = 0
      self.__zetsu: int = 0
      self.__ren: int = 0


  def _nen_baptism(self) -> None:
      if not self.__is_awakening:
          self.__is_awakening = True
          print('Seu batismo funcionou, agora pode usar nen!')
          super().__init__()
      else: print('Já está batizado!')

  def _nen_train_awake(self) -> None:
      if not self.__is_awakening and randint(self.chance, 100) == 100:
          self.__is_awakening = True
          super().__init__()
          print('Seu treino funcionou, agora pode usar nen!')
      else: self.chance += 2

  def get_ten(self):
    return self.__ten

  def get_zetsu(self):
    return self.__zetsu

  def get_ren(self):
    return self.__ren

  def get_nen_percents(self):
    if self.__is_awakening:
      for x in self._types:
        print(f'{x} - {x.get_percent()}')

  def _nen_train_zetsu(self) -> None:
    if self.__is_awakening and self.get_zetsu() < 100:
      self.__zetsu += 2
    else: print('Seu treino falhou')

  def _nen_train_ten(self) -> None:
    if self.__is_awakening and self.get_ten() < 100:
      self.__ten += 2
    else: print('Seu treino falhou')

  def _nen_train_ren(self) -> None:
    if self.__is_awakening and self.get_ren() < 100:
      self.__ren += 2
    else: print('Seu treino falhou')