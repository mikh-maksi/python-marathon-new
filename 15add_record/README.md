class Record:  
    def __init__(self):  
        self.fields = []  
    def __len__(self):  
        return len(self.fields)  
    def add(self, field_item):  
        self.fields.append(**field_item**)  