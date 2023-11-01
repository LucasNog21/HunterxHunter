from hunter import *

class Zodiac(Hunter):
    def __init__(self, animal: str, register_date: str, hunter_exam_data: str, category: str, name: str, birth_date: int) -> None:
        super().__init__(hunter_exam_data, category, name, birth_date)
        self.animal: str = animal
        self.register_date: str = register_date

    def hunting(self) -> None:
        print(f'O zôdiaco {self.name} está caçando no ambito da {self.category}')

    def meeting(self) -> None:
        print(f'Zôdiaco {self.name} está em reunião')

    def __str__(self) -> str:
        return f'Zôdiaco {self.name} o {self.animal}'