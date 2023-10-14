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

  def get_percent(self) -> int:
    return self.__percent

  def set_percent(self, new_percent) -> None :
    if new_percent in [0, 40, 60, 80, 100]:
      self.__percent = new_percent
    else: print('Valor inválido')


class Enhancement(Abstract_nen_class):
      def __init__(self) -> None:
        super().__init__()

      def __str__(self) -> str:
        return 'Enhancement'

class Transmutation(Abstract_nen_class):
      def __init__(self) -> None:
        super().__init__()
      
      def __str__(self) -> str:
        return 'Transmutation'

class Conjuration(Abstract_nen_class):
      def __init__(self) -> None:
        super().__init__()

      def __str__(self) -> str:
        return 'Conjuration'

class Emission(Abstract_nen_class):
      def __init__(self) -> None:
        super().__init__()

      def __str__(self) -> str:
        return 'Emission'

class Manipulation(Abstract_nen_class):
      def __init__(self) -> None:
        super().__init__()

      def __str__(self) -> str:
         return 'Manipulation'

class Specialization(Abstract_nen_class):
      def __init__(self) -> None:
        super().__init__()

      def __str__(self) -> str:
        return 'Specialization'

class Hatsu(Enhancement, Transmutation, Conjuration, Emission, Manipulation, Specialization):
  nen_percent_model: list[int] = [80, 60, 40, 60, 80, 100]
  list_break: int = randint(0, 5)
  def __init__(self) -> None:
        self._types: list = [Manipulation(), Emission(), Enhancement(), Transmutation(), Conjuration(), Specialization()]
        self.skill_description: str = ''
        self.skill_name: str = ''
        
        self._sort_nen_percents()

  def set_skill_name(self, name:str) -> None:
      self.skill_name = name

  def set_skill_description(self, description:str) -> None:
      self.skill_description = description

  def __random_hatsu_list(self) -> None:
      start = self._types[:self.list_break]
      end = self._types[self.list_break:]
      self._types = end + start

  def _sort_nen_percents(self) -> None:
        self.__random_hatsu_list()
        if isinstance(self._types[-1], Specialization):
          self._types[-1].set_percent(100)
        for x in range(6):
          if not isinstance(self._types[-(x+1)], Specialization):
            self._types[-(x+1)].set_percent(self.nen_percent_model[-(x+1)])