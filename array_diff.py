def array_diff(a, b):
    for i in b:
        if i in a: 
            for amt in range(a.count(i)):
                a.remove(i)
    return a

array_diff([1,2,2], [2])