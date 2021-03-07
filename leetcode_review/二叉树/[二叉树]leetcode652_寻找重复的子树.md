# [652. 寻找重复的子树](https://leetcode-cn.com/problems/find-duplicate-subtrees/)

## 描述

难度中等

给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意**一棵**的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

**示例 1：**

```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```

下面是两个重复的子树：

```
      2
     /
    4
```

和

```
    4
```

因此，你需要以列表的形式返回上述重复子树的根结点。

通过次数19,315 提交次数34,546



## 题解

> 后序遍历+序列化二叉树
>
> 后序遍历：获得当前节点的形状
>
> 序列化：将二叉树转化成字符串、以便找到相同的二叉树

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        
        memo = collections.Counter([])
        ans = []

        def builder(root):
            if not root:
                return "#"
            
            left = builder(root.left)
            right = builder(root.right)

            sub_tree = left + "," + right + "," + str(root.val)

            memo[sub_tree] += 1
            if memo[sub_tree] == 2:
                ans.append(root)
            
            return sub_tree
        
        builder(root)
        return ans
```

