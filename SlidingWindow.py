"""
模板
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

"""

"""
76. 最小覆盖子串
"""
def minWindow(s: str, t: str) -> str:
    from collections import Counter
    need, window = Counter(), Counter()

    for char in t:
        need[char] += 1
    
    left = right = 0
    valid = 0
    start = 0
    length = math.inf

    while right < len(s):
        char = s[right]
        right += 1
        if char in need:
            window[char] += 1
            if window[char] == need[char]:
                valid += 1

        while valid == len(need):
            if right - left < length:
                start = left
                length = right - left

            char = s[left]
            left += 1
            if char in need:
                if window[char] == need[char]:
                    valid -= 1
                window[char] -= 1

    if length == math.inf:
        return ""
    else:
        return s[start: start+length]