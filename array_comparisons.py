def array_comparisons(arr1, arr2):
    squares = [x**2 for x in arr1]
    for n in arr2:
        if n not in squares: 
            return False
    return True


array_comparisons([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361])

# Better way to do it:

# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False