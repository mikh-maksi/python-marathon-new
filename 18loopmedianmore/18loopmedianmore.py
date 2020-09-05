def sum(iterable):
    sum = 0
    for val in iterable:  
        sum += val  
    return sum

def avg(iterable):
    sum = 0
    n = 0
    for val in iterable:  
        sum += val
        n += 1
    return sum / n

def steps(val, step):
    result = []
    iter_number = 0  
    while iter_number <= val:  
        result.append(iter_number)  
        iter_number += step  
    return result

rate_list = [1900, 1850, 2000, 2500, 3000]  
print(sum(rate_list))
print(avg(rate_list))
print(max(rate_list))