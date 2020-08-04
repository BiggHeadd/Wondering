[TOC]

# 滑动窗口

## 脚本

### SlidingWindow.py

## 模板

```python
def slidingWindow(s: str, t: str) -> str:
    from collections import Counter
    need, window = Counter()
    for char in t:
         need[char] += 1

    # 窗口左右端点值，左闭右开
    left = right = 0
    
    # valid == len(need) -> 窗口满足条件
    valid = 0

    while right < len(s):
        # char 是将移入窗口的字符
        char = s[right]
        
        # 窗口向右拓展
        right += 1

        # 更新窗口内数据的操作
        ...

        ## debug print ##
        print("window: [{}, {})".format(left, right))
        ## debug print ##

        # 满足条件的情况下窗口左端收缩
        while valid == len(need):
            # char 是将移除窗口的字符
            char = s[left]

            # 窗口左端收缩
            left += 1

            # 更新窗口内数据的操作
            ...
```



# 二分查找

## 脚本

### BinarySearch.py

## 模板

### 寻找目标值

```python
"""
几个关键细节
    while 何时为 <=，何时为 <
        根据初始化来看，right 初始化为 len(nums) - 1，则右边界是数组最后一个元素下标，所以应当覆盖到，所以是要 <=
    
    right = mid / mid - 1
        也是根据初始化来看，right 初始化为 len(nums) - 1，则搜索的区间是左闭右闭，因此mid是已经被考虑了的，所以更新为right -> mid-1
        如果初始化为 len(nums)，则搜索区间是左闭右开，因此mid是没有被考虑到的，如果设置为mid-1，则mid-1这个值会被忽略，所以更新为right -> mid
"""

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
```

### 寻找左侧边界

```python
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
```

### 寻找右侧边界

```python
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
```



# 回溯算法

## BackTrack.py

### 核心

```python
def back_track(roads, selections):
    if condition:
        result.append(selections)
    
    for road in roads:
        if repeat or not satisfy:
            continue
        selections.append(road)
        back_track(roads, selections)
        selections.pop()
```

