def valid_parentheses(str):
    result = True
    o, c = '(', ')'
    ocount, ccount = 0, 0
    for x in str:
        if x == o: ocount += 1
        if x == c:
            ccount += 1
            if ccount > ocount: result = False
    if ocount != ccount: result = False
    print(ocount, ccount, result)

valid_parentheses('(())((()())()')

# Should have just used one count, with +1 for opening
# parentheses and -1 for closing. If val ever becomes
# negative return false, if it's not 0 at end return false.