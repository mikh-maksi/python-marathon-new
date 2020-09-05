def even(iterable):
    result = []
    for val in iterable:  
        if not val % 2:  
            result.append(val)  
    return result