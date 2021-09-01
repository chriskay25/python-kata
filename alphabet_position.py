def alphabet_position(text):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphad = {}
    for index, lttr in enumerate(alph, start = 1):
        alphad[lttr] = index
    newtext = ''

    for l in text.lower():
        if l not in alph:
            pass
        else:
            newtext = newtext + str(alphad[l]) + ' '
    
    print(newtext)

alphabet_position("The sunset sets at twelve o' clock")