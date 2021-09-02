def odd_ones_out(arr):
    evens = [x for x in arr if arr.count(x) % 2 == 0]
    print(evens)

odd_ones_out([1,2,3,1,3,3])