class Record:  
    def \_\_init\_\_(self):  
        self.fields = []  
    def add(self, field_item):  
        self.fields.append(field_item)  
    def \_\_contains\_\_(self, item: str):  
        for field in self.fields:  
            if item in **field**:  
                return True  
        return False  

