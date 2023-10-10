from random import randint

class Abstract_nen_class():
      def __init__(self) -> None:
        self._percent = 0
        self._domain = 0

      def _class_train(self):
        if self._domain < self._percent:
          if self._percent == 100:
            self._domain += 5

          elif self._percent == 60:
            self._domain += 3

          elif self._percent == 40:
            self._domain += 1

        else: print('Você atingiu seu domínio máximo!')


class Enhancement(Abstract_nen_class):
      def __init__(self):
        super().__init__()

class Transmutation(Abstract_nen_class):
      def __init__(self):
        super().__init__()

class Conjuration(Abstract_nen_class):
      def __init__(self):
        super().__init__()

class Emission(Abstract_nen_class):
      def __init__(self):
        super().__init__()

class Manipulation(Abstract_nen_class):
      def __init__(self):
        super().__init__()

class Specialization(Abstract_nen_class):
      def __init__(self):
        super().__init__()

class Hatsu(Enhancement, Transmutation, Conjuration, Emission, Manipulation, Specialization):
      descricao = ''
      list_break = randint(0, 5)
      def __int__(self) -> None:
            self._types = [Manipulation, Emission, Enhancement, Transmutation, Conjuration, Specialization]

      def sort_nen_types(self):
          start = self._types[:self.list_break]
          end = self._types[self.list_break:]
          self._types = end + start



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
              Hatsu()
          else: print('Já está batizado!')

      def _nen_train(self) -> None:
          if not self.__is_awakening and randint(self.chance, 100) == 100:
              self.__is_awakening = True
              Hatsu()
              print('Seu treino funcionou, agora pode usar nen!')
          else: self.chance += 2




teste = Nen()
teste._nen_baptism()
teste.descricao