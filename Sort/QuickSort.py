def partition(nums, left, right):
    key = nums[left]
    first = left
    last = right - 1

    while first < last:
        while first < last and nums[last] >= key:
            last -= 1

        nums[first] = nums[last]
        while first < last and nums[first] <= key:
            first += 1
        nums[last] = nums[first]

    nums[first] = key
    return first


def quick_sort(nums, left, right):
    if left + 1 >= right:
        return

    first = partition(nums, left, right)

    quick_sort(nums, left, first)
    quick_sort(nums, first + 1, right)


if __name__ == '__main__':
    nums = [7, 2, 9, 3, 5, 8, 8, 5, 1, 6, 6, 4]
    # partition(nums, 0, len(nums))
    # print(nums)
    quick_sort(nums, 0, len(nums))
    print(nums)
