# [230. 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)

## 描述

难度中等

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 个最小元素（从 1 开始计数）。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
输入：root = [3,1,4,null,2], k = 1
输出：1
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```

 

 

**提示：**

- 树中的节点数为 `n` 。
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`

 

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？



## 题解

> 二叉搜索树的中序遍历结果就是从小到大排序的结果
>
> 在中序遍历递归的过程中记录遍历到的节点序号rank，当rank=k则获得答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.rank = 0
        self.res = 0
        def traveler(root, k):
            if not root:
                return

            traveler(root.left, k)
            self.rank += 1
            if k == self.rank:
                self.res = root.val
                return
            traveler(root.right, k)
        
        traveler(root, k)
        return self.res
```

