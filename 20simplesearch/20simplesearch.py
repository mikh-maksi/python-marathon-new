class Record:
    def __init__(self):
        self.fields = []
    def add(self, field_item):
        self.fields.append(field_item)
    def __contains__(self, item: str):
        for field in self.fields:  
            if item in field:  
                return True  
        return False


a=Record()
a.add("ab")
a.add("bc123")
print(a.fields)
b= "bc" in a
print(b)