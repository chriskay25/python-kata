def count_smileys(arr):
    valid = 0
    for smiley in arr:
        if smiley[0] != ':' and smiley[0] != ';': continue
        if len(smiley) == 2:
            if smiley[1] != ')' and smiley[1] != 'D': continue
        if len(smiley) == 3:
            if smiley[1] != '-' and smiley[1] != '~': continue
            if smiley[2] != ')' and smiley[2] != 'D': continue
        valid += 1
    print(valid)
        

count_smileys([':D',':~)',';~D',':)'])