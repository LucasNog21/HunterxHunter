from Subjects.human import Human

class Hunter(Human):
    def __init__(self, hunter_exam_date: str, category:str, name: str, birth_date: int) -> None:
        super().__init__(name, birth_date)
        self.hunter_exam_date:str = hunter_exam_date
        self.category: str = category
        self.money: int = 0
        self._tiket: bool = True

    def hunting(self) -> None:
        print(f'{self.name} está caçando')

    def sell_ticket(self) -> None:
        if self._tiket:
            self.money += 100_000
            self._tiket = False

            print(f"{self.name} não tem mais sua liçença hunter, mas ganhou uma boa grana.")

    def __str__(self) -> str:
        return f'Hunter {self.category} : {self.name}'
