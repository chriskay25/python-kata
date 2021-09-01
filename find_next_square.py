def find_next_square(sq):
    root = sq ** .5
    vals = root.as_integer_ratio()
    if vals[1] == 1:
        return (vals[0] + 1) ** 2
    else:
        return -1


find_next_square(16)