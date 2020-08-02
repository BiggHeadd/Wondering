"""
模板
def slidingWindow(s: str, t: str) -> str:
    from collections import Counter
    need, window = Counter()
    for c in t:
         need[c] += 1

    # 窗口左右端点值，左闭右开
    left = right = 0
    
    # valid == len(need) -> 窗口满足条件
    valid = 0

    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        
        # 窗口向右拓展
        right += 1

        # 更新窗口内数据的操作
        ...

        ## debug print ##
        print("window: [{}, {})".format(left, right))
        ## debug print ##

        # 满足条件的情况下窗口左端收缩
        while valid == len(need):
            # d 是将移除窗口的字符
            d = s[left]

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
    for c in t:
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
        c = s[right]
        # 窗口向右拓展
        right += 1
        # 对于窗口内的数据进行更新
        if c in need:
            # 子串所需字符标记+1
            window[c] += 1
            # 如果已满足，valid += 1
            if window[c] == need[c]:
                valid += 1

        # 当已经满足覆盖了子串，窗口左端收缩，寻找最小覆盖子串
        while valid == len(need):
            # 如果子串比记录值小，记录下作为最小覆盖子串
            if right - left < length:
                start = left
                length = right - left

            # 即将移出窗口的左端点值
            d = s[left]
            # 窗口左端收缩
            left += 1
            # 如果移出的是覆盖子串的字符
            if d in need:
                # 如果移出当前之后就不满足该字符覆盖，valid -= 1
                if window[d] == need[d]:
                    valid -= 1
                # 覆盖窗口的字符记录值-1
                window[d] -= 1

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
            
            d = s2[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return False


"""
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

---------------------------------------------------------------
输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

---------------------------------------------------------------
输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

"""
def findAnagrams(s: str, p: str) -> List[int]:
    from collections import Counter
    need, window = Counter(), Counter()

    for c in p:
        need[c] += 1

    left = right = 0
    valid = 0
    result = []

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while right - left >= len(p):
            if valid == len(need):
                result.append(left)
            
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return result


"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

---------------------------------------------------------------
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

---------------------------------------------------------------
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

---------------------------------------------------------------
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

def lengthOfLongestSubstring(s: str) -> int:
    from collections import Counter
    window = Counter()
    
    left = right = 0
    result = 0

    while right < len(s):
        c = s[right]
        right += 1

        window[c] += 1

        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1

        result = max(result, right-left)
    return result