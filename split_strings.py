def split_strings(s):
    result = []
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    if len(i) == 1:
        result[-1] = i + '_'
    print(result)

split_strings('abcdefg')