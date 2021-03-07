# [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## 描述

难度中等

根据一棵树的前序遍历与中序遍历构造二叉树。

**注意:**
你可以假设树中没有重复的元素。

例如，给出

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

通过次数160,297

提交次数231,403



## 题解

> 前序遍历构造
>
> 1. preorder列表的首位是二叉树的根节点
> 2. 根节点在inorder列表中将左右子树分割为列表左右两部分
> 3. 递归构造左右子树

```python
## 耗时：188 ms
## builder函数直接传递preorder、inorder列表

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        def builder(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root_val = preorder[0]
            root = TreeNode(root_val)

            root_val_index = inorder.index(root_val)
            left_length = root_val_index

            root.left = builder(preorder[1:1+left_length], inorder[:left_length])
            root.right = builder(preorder[1+left_length:], inorder[root_val_index+1:])

            return root

        root = builder(preorder, inorder)
        return root
```



```python
## 耗时：56 ms
## builder传递preorder、inorder列表的左右下标，inorder列表的元素->下标提前计算好
## 下标的传递需要注意细节

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        def builder(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)

            root_val_index = index[root_val]
            left_length = root_val_index - inorder_left

            root.left = builder(preorder_left+1, preorder_left+left_length, inorder_left, root_val_index-1)
            root.right = builder(preorder_left+1+left_length, preorder_right, root_val_index+1, inorder_right)
            # preorder[1+left_length:], inorder[root_val_index+1:]

            return root

        n = len(preorder)
        index = {element: index for index, element in enumerate(inorder)}
        root = builder(0, n-1, 0, n-1)
        return root
```

