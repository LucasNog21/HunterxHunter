class Treath:
    def __init__(self, specie, level):
        self.specie = specie
        self.__level = level
    
    def set_level(self,new_level):
        self.__level = new_level
    
    def get_level(self):
        return self.__level
    