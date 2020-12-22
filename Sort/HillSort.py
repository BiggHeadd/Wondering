def hill_sort(nums):
    length = len(nums)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j, cur = i, nums[i]
            while (j-gap >= 0) and (cur < nums[j-gap]):
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = cur
        gap = gap // 2


if __name__ == '__main__':
    nums_main = [7, 2, 9, 3, 5, 8, 8, 5, 1, 6, 6, 4]
    hill_sort(nums_main)
    print(f"hill sort: {nums_main}")