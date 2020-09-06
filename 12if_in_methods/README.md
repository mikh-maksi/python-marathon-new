# Оператор выбора
## Код задачи

import re  
class DataField:  
&nbsp;&nbsp;&nbsp;&nbsp;field_description = "General data"  

&nbsp;&nbsp;&nbsp;&nbsp;def \_\_init\_\_(self, value):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.value = None  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.validate(value)  

&nbsp;&nbsp;&nbsp;&nbsp;def validate(self, value):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.value = value  

&nbsp;&nbsp;&nbsp;&nbsp;def \_\_contains\_\_(self, item):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return item in self.value  

&nbsp;&nbsp;&nbsp;&nbsp;def \_\_str\_\_(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return f"{self.field_description}: {self.value}"  


class EmailField(DataField):  
&nbsp;&nbsp;&nbsp;&nbsp;field_description = "Email"  
&nbsp;&nbsp;&nbsp;&nbsp;EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")  

&nbsp;&nbsp;&nbsp;&nbsp;def validate(self, value):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if **self.EMAIL_REGEX.match(value)**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.value = value  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print (f"email changed to {value}.")  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print (f"{value} is not an email.")  


a = EmailField("")
a.validate("mikhail_maksimov@goit.ua")

print("ok")
