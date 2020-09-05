class IncorrectInput(Exception):  
    pass  
class DataField:  
    field_description = "General data"  
    def __init__(self, value):  
        self.value = None  
        self.validate(value)  
    def validate(self, value):  
        self.value = value  
    def __contains__(self, item):  
        return item in self.value  
    def __str__(self):  
        return f"{self.field_description}: {self.value}"  
class RateField(DataField):  
    def validate(self, value):  
        try:  
            self.value = float(value)  
        except ValueError:  
            raise IncorrectInput(**f"value {value} can't be converted to float"**)  