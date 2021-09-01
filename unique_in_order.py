def unique_in_order(iterable):
    if type(iterable) == str: iterable = list(iterable)
    prev, current = 0, 1
    while len(iterable) > current:
        if iterable[current] == iterable[prev]:
            del iterable[prev]
        else:
            prev += 1
            current += 1
    return iterable

unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD') 
unique_in_order([1,2,2,3,3])