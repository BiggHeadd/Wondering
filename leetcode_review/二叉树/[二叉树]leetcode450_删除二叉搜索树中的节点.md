# [450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/)

## 描述

难度中等

给定一个二叉搜索树的根节点 **root** 和一个值 **key**，删除二叉搜索树中的 **key** 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

1. 首先找到需要删除的节点；
2. 如果找到了，删除它。

**说明：** 要求算法时间复杂度为 O(h)，h 为树的高度。

**示例:**

```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
```

通过次数34,985 提交次数75,553



## 题解

> 1. node.val > key，递归左子树
> 2. node.val < key，递归右子树
> 3. node.val = key，删除当前节点
>    1. 当没有左右子树时，直接删除节点
>    2. 当存在右子树时，查找右子树中最小的节点，替换当前节点，并递归右子树删除最小的节点
>    3. 当存在左子树时，查找左子树中最大的节点，替换当前节点，并递归左子树删除最大的节点

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        def find_successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val
        
        def find_predecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val
        
        def delete(node, key):
            if not node:
                return None

            tmp = node.val
            if key > tmp:
                node.right = delete(node.right, key)
            elif key < tmp:
                node.left = delete(node.left, key)
            else:
                if not node.left and not node.right:
                    node = None
                elif node.right:
                    node.val = find_successor(node)
                    node.right = delete(node.right, node.val)
                else:
                    node.val = find_predecessor(node)
                    node.left = delete(node.left, node.val)
            return node
        return delete(root, key)
```

