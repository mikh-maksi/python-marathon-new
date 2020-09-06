# Магические методы
Магические методы - это методы, которые переопределяют операции, которые производятся с экземплярами класса. В том числе - это операции сравнения.  
Зачем это нужно?
В распряжении у программиста имеется большой набор инструментов, который доступен и пределен для типов данных: операции сравнения, математические операции. Сами по себе такие операции не определены для объектов новых классов. Для того, чтобы определить такие операции и используются магические методы. Т.е. просто по-умолчанию сравнения двух объектов метода *Record* будет вызывать ошибку. А если в классе Record описать соответствующие методы, то такими операциями можно будет пользоваться. Программист в таком методе, по сути, говорит, по каким параметрам сравнивать объекты соответствующего класса.


 def __eq__(self, other):  = 
 def __gt__(self, other):  >
 def __lt__(self, other):  <

Использование магических методов позволяет сравнивать объекты. Результатом сравнения всегда будет значение булевого типа: True (истина) или False (ложь).  

Булев тип - является понятием очень важными для оператора выбора. Это такая управляющая конструкция, которая позволяет выполнять часть команд, только при выполнении определенного условия.
Например:
if a>0:
    print("число а - положительное")

Результаты таких операций удобно использовать для операторов выбора: если сравнение возвращает результат True, то и оператор выбора 

## Текст задачи
class Record:  
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_init\_\_(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.fields = []  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.name = "Oleg"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.phone = "+380631234567"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.skill = "Python"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.city = "Kyiv"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.rate = 2000  

&nbsp;&nbsp;&nbsp;&nbsp;def \_\_eq\_\_(self, other):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self.rate == other.rate    
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_gt\_\_(self, other):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self.rate **>** other.rate  
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_lt\_\_(self, other):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self.rate < other.rate  

b = Record()  
c = Record()  
c.name = "Igor"  
c.rate = 3000  

if c>b:  
    print (f"{c.name} зарабатывает больше чем {b.name}")  

