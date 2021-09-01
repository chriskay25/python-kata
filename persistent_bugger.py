import math

def persistent_bugger(n):
    persistence = 0
    resolved = False
    while resolved == False:
        dgts = [int(dgt) for dgt in str(n)]
        product = math.prod(dgts)
        dgts = [int(dgt) for dgt in str(product)]
        if len(dgts) == 1:
            persistence += 1
            resolved = True
        else:
            persistence += 1
            n = product
    print(persistence)

persistent_bugger(39)