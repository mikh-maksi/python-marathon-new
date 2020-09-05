class IncorrectInput(Exception):
    pass
def index_error_decorator(function):
    def inner(*args):
        try:
            result = function(*args)
            return result
        except IndexError:
            raise IncorrectInput(f"Запис не містить такого індексу")
        except ValueError:
            raise IncorrectInput(f"Передане значення індексу не є цілим числом")
    return inner
class Record:
    def __init__(self):
        self.fields = []
    def __len__(self):
        return len(self.fields)
    def add(self, field_item):
        self.fields.append(field_item)
    @index_error_decorator
    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)
    @index_error_decorator
    def update(self, field_idx, value):
        field_idx = int(field_idx)
        field = self.fields[field_idx]
        field.validate(value)
    def __contains__(self, item: str):
        for field in self.fields:  
            if item in field:  
                return True  
        return False