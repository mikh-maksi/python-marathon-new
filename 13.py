class IncorrectInput(Exception):
    pass

class Record:
    def __init__(self):
        self.fields = [] #self.fields = - при создании экземпляра класса - создает пустой список
    
    def add(self, field_item):
        self.fields.append(field_item) #self.fields.append() к списку fields добавляется элемент field_item
