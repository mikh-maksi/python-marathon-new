class IncorrectInput(Exception):  
    pass  
class Record:  
    def \_\_init\_\_(self):  
        self.fields = []  
    def \_\_len\_\_(self):  
        return len(self.fields)  
    def add(self, field_item):  
        self.fields.append(field_item)  
    def delete(self, idx):  
        try:  
            idx = int(idx)  
            self.fields.pop(**idx**)  
        except IndexError:  
            raise IncorrectInput(f"Запис не містить поля з індексом {idx}")  
        except ValueError:  
            raise IncorrectInput(f"Передане значення '{idx}' не є цілим числом")  