def selection_sort(nums):
    length = len(nums)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]


if __name__ == '__main__':
    nums_main = [7, 2, 9, 3, 5, 8, 8, 5, 1, 6, 6, 4]
    selection_sort(nums_main)
    print(f"selection sort: {nums_main}")
