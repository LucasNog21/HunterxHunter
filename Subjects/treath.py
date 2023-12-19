class Treath:
    def __init__(self, name, specie, level):
        self.name = name
        self.specie = specie
        self.__level = level
    
    def set_level(self,new_level):
        self.__level = new_level
    
    def get_level(self):
        return self.__level
    