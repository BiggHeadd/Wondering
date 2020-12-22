import collections

def merge(L, R):
    n = len(L) + len(R)
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    A = []
    for index in range(n):
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1
    return A


def merge_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums

    mid = length // 2
    left_part = merge_sort(nums[0:mid])
    right_part = merge_sort(nums[mid:])

    return merge(left_part, right_part)


def merge_(left, right):
    res = []
    left = collections.deque(left)
    right = collections.deque(right)
    while left and right:
        min_val = left.popleft() if left[0] < right[0] else right.popleft()
        res.append(min_val)
    res += left if left else right
    return res


def merge_sort_(nums):
    length = len(nums)
    if length <= 1:
        return nums

    mid = length // 2
    left, right = merge_sort_(nums[:mid]), merge_sort_(nums[mid:])
    return merge_(left, right)


if __name__ == '__main__':
    nums_main = [7, 2, 9, 3, 5, 8, 8, 5, 1, 6, 6, 4]

    print("solution #1")
    ans = merge([1, 5, 6], [2, 3])
    print(f"merge result: {ans}")
    ans = merge_sort(nums_main)
    print(f"merge sort result: {ans}")

    print("solution #2")
    ans = merge_([1, 5, 6], [2, 3])
    print(f"merge result: {ans}")
    ans = merge_sort_(nums_main)
    print(f"merge sort result: {ans}")
