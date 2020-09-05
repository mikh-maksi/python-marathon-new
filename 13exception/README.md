a = 5  
b = 0  
try:   
    c=a/b  
except ZeroDivisionError:  
    print("Ошибка деления на ноль. Переменная c получила значение a")  
    c = **a** 

print(c)