class Record:  
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_init\_\_(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.fields = []  
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_len\_\_(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return len(self.fields)  
&nbsp;&nbsp;&nbsp;&nbsp;def add(self, field_item):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.fields.append(**field_item**)  