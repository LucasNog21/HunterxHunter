from Subjects.hunter import Hunter

class User(Hunter):
    def __init__(self, username: str, password: str, hunter_exam_date: str, category:str, name: str, birth_date: int):
        super().__init__(hunter_exam_date, category, name, birth_date)
        self.username: str = username
        self.__password: str = password
    
    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password


    
    

