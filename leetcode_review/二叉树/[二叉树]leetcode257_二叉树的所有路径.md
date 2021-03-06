# [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)

## 描述

难度简单

给定一个二叉树，返回所有从根节点到叶子节点的路径。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

```
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
```

通过次数98,936 提交次数148,462



## 题解

> 先遍历根的方式——先序遍历
>
> tmp记录路径
>
> 到达叶子节点的时候记录

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        ans = []
        tmp = []

        def builder(root, tmp):
            if not root:
                return

            tmp.append(str(root.val))            
            if not root.left and not root.right:
                ans.append("->".join(tmp))

            builder(root.left, tmp)
            builder(root.right, tmp)
            tmp.pop()

        builder(root, tmp)
        return ans
```

