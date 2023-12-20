
class Data_report:
    def __init__(self, title, category, description, name):
        self.title = title
        self.category = category
        self.description = description
        self.__name = name

    def get_name(self):
        return self.__name