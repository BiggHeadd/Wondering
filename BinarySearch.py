"""
二分搜索的模板

1. 寻找目标值

几个关键细节
    while 何时为 <=，何时为 <
        根据初始化来看，right 初始化为 len(nums) - 1，则右边界是数组最后一个元素下标，所以应当覆盖到，所以是要 <=
    
    right = mid / mid - 1
        也是根据初始化来看，right 初始化为 len(nums) - 1，则搜索的区间是左闭右闭，因此mid是已经被考虑了的，所以更新为right -> mid-1
        如果初始化为 len(nums)，则搜索区间是左闭右开，因此mid是没有被考虑到的，如果设置为mid-1，则mid-1这个值会被忽略，所以更新为right -> mid

def binarySearch(nums: list, target: int) -> bool:
    if not nums:
        return Flase

    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return True


2. 寻找左侧边界


def left_bound(nums: list, target: int) -> int:
    if not nums:
        return -1
    
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            # 向左继续寻找左侧边界
            right = mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    
    if left == len(nums):
        return -1
    if nums[left] == target:
        return left
    else:
        return -1

3. 寻找右边界

def right_bound(nums: list, target: int) -> int:
    if not nums:
        return -1
    
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 向右继续寻找右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    
    if left == 0:
        return -1
    if nums[left - 1] == target:
        return left - 1
    else:
        return -1
"""


"""
29. 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

---------------------------------------------------------------
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

---------------------------------------------------------------
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

---------------------------------------------------------------
提示：
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2**31,  2**31 − 1]。本题中，如果除法结果溢出，则返回 2**31 − 1。
"""

def divide(dividend: int, divisor: int) -> int:
    """
    此题实际上为最基本的二分查找值 + 第一个大于目标值的值查找 问题，只不过查找目标为 除数*二分过程中的mid
    当能正好有mid可以整除的时候，则为二分查找值
    如果没有，则查找第一个大于 目标值 的 除数*mid
    """

    # 应对负数情况，二分搜索的时候采用正数，最终结果再转化为负数
    if dividend < 0 and divisor < 0:
        flag = False
    elif dividend > 0 and divisor < 0:
        flag = True
    elif dividend < 0 and divisor > 0:
        flag = True
    else:
        flag = False
    
    dividend = abs(dividend)
    divisor = abs(divisor)

    left = 0
    right = dividend + 1
    while left < right:
        mid = left + (right - left) // 2
        mul = mid * divisor
        if mul < dividend:
            # 
            left = mid + 1
        elif mul > dividend:
            right = mid
        elif mul == dividend:
            # 刚好整除
            if flag:
                # 应对溢出，python中不会溢出，但是leetcode题目的解是在非溢出范围内的，要手动限制结果的范围
                if mid > 2**31:
                    mid = 2**31
                return mid * (-1)
            else:
                if mid > 2**31-1:
                    mid = 2**31-1
                return mid
    if flag:
        # 应对溢出，python中不会溢出，但是leetcode题目的解是在非溢出范围内的，要手动限制结果的范围
        if (left - 1) > 2**31:
            left = 2**31 + 1
        return (left - 1) * -1
    else:
        if (left - 1) > 2**31-1:
            left = 2**31
        return left - 1