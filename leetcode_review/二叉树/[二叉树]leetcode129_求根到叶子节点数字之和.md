# [129. 求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)

## 描述

难度中等

给定一个二叉树，它的每个结点都存放一个 `0-9` 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 `1->2->3` 代表数字 `123`。

计算从根到叶子节点生成的所有数字之和。

**说明:** 叶子节点是指没有子节点的节点。

**示例 1:**

```
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
```

**示例 2:**

```
输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
```

通过次数84,854 提交次数127,278



## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        nums = []
        tmp = []
        def get_sum(root, tmp):
            if not root:
                return
            
            tmp.append(str(root.val))
            if not root.left and not root.right:
                nums.append(int("".join(tmp[:])))
            
            get_sum(root.left, tmp)
            get_sum(root.right, tmp)
            tmp.pop()

        get_sum(root, tmp)
        return sum(nums)
```



> 优化求和计算、总和nums初始化方式，
>
> 执行结果：通过
>
> 执行用时：32 ms, 在所有 Python3 提交中击败了97.00%的用户
>
> 内存消耗：15.1 MB, 在所有 Python3 提交中击败了22.89%的用户

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = 0
        
    def sumNumbers(self, root: TreeNode) -> int:
        def get_sum(root, cur):
            if not root:
                return
            
            cur = cur*10 + root.val
            if not root.left and not root.right:
                self.nums += cur
                return
            
            get_sum(root.left, cur)
            get_sum(root.right, cur)

        get_sum(root, 0)
        return self.nums
```