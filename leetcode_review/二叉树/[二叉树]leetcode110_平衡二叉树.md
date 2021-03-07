# [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

## 描述

难度简单

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

> 一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1 。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：true
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
```

**示例 3：**

```
输入：root = []
输出：true
```

 

**提示：**

- 树中的节点数在范围 `[0, 5000]` 内
- `-104 <= Node.val <= 104`

通过次数179,095 提交次数323,792



## 题解

> 左右根的后序遍历
>
> 需要根据左右子树的深度进行判断，在不满足的时候将深度设置为-1返回

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def judger(root):
            if not root:
                return 0
            
            left = judger(root.left)
            right = judger(root.right)

            if left == -1 or right == -1 or abs(left-right)>1:
                return -1
            
            return max(left, right) + 1
        
        ans = judger(root)
        if ans == -1:
            return False
        else:
            return True
```