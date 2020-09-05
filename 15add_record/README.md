class Record:  
    def \_\_init\_\_(self):  
        self.fields = []  
    def \_\_len\_\_(self):  
        return len(self.fields)  
    def add(self, field_item):  
        self.fields.append(**field_item**)  