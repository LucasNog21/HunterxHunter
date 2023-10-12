from random import randint

class Abstract_nen_class():
  def __init__(self) -> None:
    self.__percent = 0
    self.__domain = 0

  def _class_train(self) -> None:
    if self._domain < self._percent:
      if self.__percent == 100:
        self.__domain += 5

      elif self.__percent == 60:
        self.__domain += 3

      elif self.__percent == 40:
        self.__domain += 1
    else: print('Você atingiu seu domínio máximo!')

  def get_percent(self):
    return self.__percent

  def set_percent(self, new_percent) -> None :
    if new_percent in [0, 40, 60, 80, 100]:
      self.__percent = new_percent
    else: print('Valor inválido')


class Enhancement(Abstract_nen_class):
      def __init__(self):
        super().__init__()

      def __str__(self) -> str:
        return 'Enhancement'

class Transmutation(Abstract_nen_class):
      def __init__(self):
        super().__init__()
      
      def __str__(self) -> str:
        return 'Transmutation'

class Conjuration(Abstract_nen_class):
      def __init__(self):
        super().__init__()

      def __str__(self) -> str:
        return 'Conjuration'

class Emission(Abstract_nen_class):
      def __init__(self):
        super().__init__()

      def __str__(self) -> str:
        return 'Emission'

class Manipulation(Abstract_nen_class):
      def __init__(self):
        super().__init__()

      def __str__(self) -> str:
         return 'Manipulation'

class Specialization(Abstract_nen_class):
      def __init__(self):
        super().__init__()

      def __str__(self) -> str:
        return 'Specialization'

class Hatsu(Enhancement, Transmutation, Conjuration, Emission, Manipulation, Specialization):
  descricao = ''
  nen_percent_model = [80, 60, 40, 60, 80, 100]
  list_break = randint(0, 5)
  def __init__(self) -> None:
        self._types = [Manipulation(), Emission(), Enhancement(), Transmutation(), Conjuration(), Specialization()]
        
        self._sort_nen_percents()

  def __random_hatsu_lsit(self):
      start = self._types[:self.list_break]
      end = self._types[self.list_break:]
      self._types = end + start

  def _sort_nen_percents(self):
        self.__random_hatsu_lsit()
        if isinstance(self._types[-1], Specialization):
          self._types[-1].set_percent(100)
        for x in range(6):
          if not isinstance(self._types[-(x+1)], Specialization):
            self._types[-(x+1)].set_percent(self.nen_percent_model[-(x+1)])


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

teste = Nen()
teste._nen_baptism()
teste.get_nen_percents()