# [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)

## 描述

难度中等

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含**小于**当前节点的数。
- 节点的右子树只包含**大于**当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

**示例 1:**

```
输入:
    2
   / \
  1   3
输出: true
```

**示例 2:**

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

通过次数229,605 提交次数681,610



## 题解

> 分别判断左右子树是否满足BST树 --> 左右中，后序遍历
>
> BST：左子树均比根小，右子树均比根大

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False

        def judger(root, minimal, maxmal):
            if not root:
                return True

            if minimal and root.val <= minimal.val:
                return False
            
            if maxmal and root.val >= maxmal.val:
                return False
            
            left_valid = judger(root.left, minimal, root)
            right_valid = judger(root.right, root, maxmal)
        
            return left_valid and right_valid
        
        valid = judger(root, None, None)
        
        return valid
```

