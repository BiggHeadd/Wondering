def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        pointer = i - 1
        cur = nums[i]
        while pointer >= 0 and nums[pointer] > cur:
            nums[pointer + 1] = nums[pointer]
            pointer -= 1
        nums[pointer + 1] = cur


if __name__ == '__main__':
    nums_main = [7, 2, 9, 3, 5, 8, 8, 5, 1, 6, 6, 4]
    insert_sort(nums_main)
    print(f"insert sort: {nums_main}")
