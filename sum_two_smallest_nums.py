def sum_two_smallest_nums(nums):
    smallest = min(nums)
    nums.remove(smallest)
    return smallest + min(nums)

sum_two_smallest_nums([19, 5, 42, 2, 77])