from random import choice
from human import Human

class ChimeraAnt(Human):
    def __init__(self, name: str, first_animal: str, second_animal: str, birth_date: str) -> None:
        self.name: str = name
        self.first_animal: str = first_animal
        self.second_animal: str = second_animal
        self.__birth_date: str = birth_date

        self._can_use_nen()

    def get_birth_date(self) -> int:
        return self.__birth_date

    def _can_use_nen(self) -> None:
        if self.first_animal == 'human':
            Human.__init__(self, self.name, self.get_birth_date())

    def __str__(self) -> str:
        return super().__str__()

class ChimeraQueen():
    def __init__(self, name:str , birth_date: str) -> None:
        self.name: str = name
        self.__birth_date: str = birth_date
        self._belly: list[str] = []
        self.chields : list[ChimeraAnt] = []

    def get_birth_date(self) -> str:
        return self.__birth_date
    
    def eat(self, food:str) -> None:
        self._belly.append(food.lower())
        print(f'Nhum nhum, a rainha {self} comeu {food}')

    def having_children(self, name, birth_date) -> None:
        if 'human' in self._belly or 'humano' in self._belly:
            chield = ChimeraAnt(name, 'human', choice(self._belly), birth_date)
            print(f'''A rainha {self.name} teve um filho quimera
                  de humano com {chield.second_animal}
                  chamado {chield.name} que pode usar nen''')
        else:
            chield = ChimeraAnt(name, choice(self._belly), choice(self._belly), birth_date)
            print(f'''A rainha {self.name} teve um filho quimera
                  de {chield.first_animal} com {chield.second_animal}
                  chamado {chield.name} ''')
        self.chields.append(chield)

    def __str__(self) -> str:
        return f'{self.name}'
    