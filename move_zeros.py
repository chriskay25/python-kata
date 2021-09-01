# def move_zeros(arr):
#     for idx, i in enumerate(arr):
#         if i == 0:
#             print('%s is a zero' %i)
#             del arr[idx]
#             arr.append(i)
#     print(arr)

# # move_zeros([1,0,1,2,0,1,3])
# move_zeros([2,0,2,0])

# Above works but wasn't accepted due to arbitrary test rules

def move_zeros(arr):
    new_arr = []
    zeros_count = 0
    for i in arr:
        if i != 0:
            new_arr.append(i)
        else:
            zeros_count = zeros_count + 1
    for zero in range(zeros_count):
        new_arr.append(0)
    print(new_arr)

move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0])
