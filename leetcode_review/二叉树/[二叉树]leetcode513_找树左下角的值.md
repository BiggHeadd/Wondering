# [513. 找树左下角的值](https://leetcode-cn.com/problems/find-bottom-left-tree-value/)

## 描述

难度中等

给定一个二叉树，在树的最后一行找到最左边的值。

**示例 1:**

```
输入:

    2
   / \
  1   3

输出:
1
```

 

**示例 2:**

```
输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
```

**注意:** 您可以假设树（即给定的根节点）不为 **NULL**。

通过次数30,491 提交次数42,075



## 题解

>右节点入队列，左节点再入队列

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        node = None
        while len(queue) > 0:
            node = queue.popleft()
        
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return node.val
```

