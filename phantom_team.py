from human import Human

class PhantomTeamMember(Human):
    def __init__(self, register_date: str, name: str, birth_date: int) -> None:
        super().__init__(name, birth_date),
        self.register_date: str = register_date
        self.__number = 0
        self.__is_leader: bool = False

    def set_number(self, number) -> None:
        if number in range(1, 13):
            self.__number = number
        else: print('Numero inválido')

    def _become_leader(self) -> None:
        if not self.__is_leader:
            self.__is_leader = True

    def stealing(self, victim) -> None:
        print(f'{self.name} is stealing {victim}')

    def __str__(self) -> str:
        return f'Trupe fantasma número {self.number} : {self.name}'