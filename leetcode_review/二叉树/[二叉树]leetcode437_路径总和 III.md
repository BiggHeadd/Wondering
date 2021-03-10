# [437. 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii/)

## 描述

难度中等

给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

**示例：**

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
```

通过次数68,391 提交次数120,812



## 题解

>前缀和
>
>统计根到当前节点的前缀和，判断当前和与目标值的差值是否出现过
>
>后序遍历返回上层时，需要回退记录中前缀和计数以及前缀和

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        cur_sum = 0
        memo = collections.Counter()
        memo[0] += 1
        ans = 0
        def finder(node, memo, target):
            if not node:
                return
            
            nonlocal ans, cur_sum
            cur_sum += node.val
            if cur_sum - target in memo:
                ans += memo[cur_sum-target]
            memo[cur_sum] += 1
            finder(node.left, memo, target)
            finder(node.right, memo, target)

            memo[cur_sum] -= 1
            cur_sum -= node.val
        finder(root, memo, sum)
        return ans
```

