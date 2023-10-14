from nen import Nen

class Human(Nen):
    def __init__(self, name: str, birth_date: int) -> None:
        super().__init__()
        self.name: str = name
        self.__birth_date:int = birth_date

    def get_birth_date(self):
        return self.__birth_date

    def __str__(self) -> str:
        return f"{self.name}"
    
    def use_skill(self, victim):
        print(f"{self.name} usou sua habilidade: {self.skill_name} em {victim}")