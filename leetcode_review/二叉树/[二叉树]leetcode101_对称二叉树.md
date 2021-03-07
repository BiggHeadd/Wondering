# [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/)

## 描述

难度简单

给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 `[1,2,2,3,4,4,3]` 是对称的。

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

 

但是下面这个 `[1,2,2,null,3,null,3]` 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```

 

**进阶：**

你可以运用递归和迭代两种方法解决这个问题吗？

通过次数275,351 提交次数511,417



## 题解

> 同时对二叉树进行`root->left->right`和`root->right->left`的遍历，判断遍历到的每个值是否相等。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def judger(node_left, node_right):
            if not node_left and not node_right:
                return True
            
            if node_left and node_right and node_left.val == node_right.val:
                return judger(node_left.left, node_right.right) and judger(node_left.right, node_right.left)
            
            return False
        
        return judger(root.left, root.right)
```

