def bubble_sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == '__main__':
    nums_main = [7, 2, 9, 3, 5, 8, 8, 5, 1, 6, 6, 4]
    bubble_sort(nums_main)
    print(f"bubble sort: {nums_main}")
