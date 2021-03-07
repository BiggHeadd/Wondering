# [106. 从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## 描述

难度中等

根据一棵树的中序遍历与后序遍历构造二叉树。

**注意:**
你可以假设树中没有重复的元素。

例如，给出

```
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
```

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

通过次数91,767 提交次数128,700



## 题解

> 前序遍历构造
>
> 1. postorder列表最后一位是根，根将inorder列表分割成左右子树列表
> 2. 不断取postorder最后一位，作为右子树的根
> 3. 递归构造右子树、左子树

```python
## 耗时：208 ms
## builder传递inorder、postorder数组，其中的root_val_index需要实时计算（比较耗时）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        def builder(inorder, postorder):
            if not inorder or not postorder:
                return None
            
            root_val = postorder.pop()
            root_val_index = inorder.index(root_val)
            left_tree_size = root_val_index

            root = TreeNode(root_val)

            root.right = builder(inorder[root_val_index+1:], postorder[left_tree_size:])
            root.left = builder(inorder[:root_val_index], postorder[:left_tree_size])

            return root

        n = len(inorder)
        root = builder(inorder, postorder)
        return root
```



```python
## 耗时：44 ms
## builder传递inorder数组下标，不断pop出postorder列表元素

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_index_in_inorder = index[root_val]

            root.right = build(root_index_in_inorder+1, inorder_right)
            root.left = build(inorder_left, root_index_in_inorder-1)

            return root

        index = {value: i for i, value in enumerate(inorder)}
        return build(0, len(inorder)-1)
```

