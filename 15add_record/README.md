class Record:  
    def \__init_\_(self):  
        self.fields = []  
    def \__len_\_(self):  
        return len(self.fields)  
    def add(self, field_item):  
        self.fields.append(**field_item**)  