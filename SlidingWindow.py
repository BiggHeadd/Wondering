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

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

---------------------------------------------------------------
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""
def minWindow(s: str, t: str) -> str:
    from collections import Counter
    need, window = Counter(), Counter()

    # 初始化子串所涵盖的字符及数量
    for char in t:
        need[char] += 1
    
    # 左右窗口值
    left = right = 0
    # 已包含的字符数
    valid = 0
    # 匹配到的最小覆盖子串的开始端点
    start = 0
    # 匹配到的最小覆盖子串的长度
    length = math.inf

    while right < len(s):
        # 即将进入窗口的字符
        char = s[right]
        # 窗口向右拓展
        right += 1
        # 对于窗口内的数据进行更新
        if char in need:
            # 子串所需字符标记+1
            window[char] += 1
            # 如果已满足，valid += 1
            if window[char] == need[char]:
                valid += 1

        # 当已经满足覆盖了子串，窗口左端收缩，寻找最小覆盖子串
        while valid == len(need):
            # 如果子串比记录值小，记录下作为最小覆盖子串
            if right - left < length:
                start = left
                length = right - left

            # 即将移出窗口的左端点值
            char = s[left]
            # 窗口左端收缩
            left += 1
            # 如果移出的是覆盖子串的字符
            if char in need:
                # 如果移出当前之后就不满足该字符覆盖，valid -= 1
                if window[char] == need[char]:
                    valid -= 1
                # 覆盖窗口的字符记录值-1
                window[char] -= 1

    if length == math.inf:
        return ""
    else:
        return s[start: start+length]


"""
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

---------------------------------------------------------------
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
"""

def checkInclusion(s1: str, s2: str) -> bool:
    from collections import Counter
    need, window = Counter(), Counter()

    for c in s1:
        need[c] += 1
    
    left = right = 0
    valid = 0

    while right < len(s2):
        c = s2[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 因为排列是要长度是一样的，所以当大于等于（其实只会触及等于，不会触及大于）的时候，就要缩小窗口
        while right - left >= len(s1):
            # 当每个字符都覆盖到的时候，说明满足条件，返回True
            if valid == len(need):
                return True
            
            c = s2[left]
            left += 1
            if c in need:
                if window[c] == need[c]:
                    valid -= 1
                window[c] -= 1
    return False