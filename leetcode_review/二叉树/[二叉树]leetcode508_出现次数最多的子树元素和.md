# [508. 出现次数最多的子树元素和](https://leetcode-cn.com/problems/most-frequent-subtree-sum/)

## 描述

难度中等

给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

 

**示例 1：**
输入:

```
  5
 /  \
2   -3
```

返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

**示例 2：**
输入：

```
  5
 /  \
2   -5
```

返回 [2]，只有 2 出现两次，-5 只出现 1 次。

 

**提示：** 假设任意子树元素和均可以用 32 位有符号整数表示。

通过次数11,088 提交次数16,805



## 题解

> 对每个节点求子树和，记录freq

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        counter = collections.Counter()
        max_freq = 0

        def builder(node):
            if not node:
                return 0
            
            left_sum = builder(node.left)
            right_sum = builder(node.right)
            root_sum = left_sum + node.val + right_sum
            counter[root_sum] += 1
            
            nonlocal max_freq
            max_freq = max(max_freq, counter[root_sum])

            return root_sum

        builder(root)
        ans = []
        for key, value in counter.items():
            if value == max_freq:
                ans.append(key)
        return ans
```