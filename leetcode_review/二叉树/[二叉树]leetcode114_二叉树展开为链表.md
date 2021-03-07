# [114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)

## 描述

难度中等

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
- 展开后的单链表应该与二叉树 [**先序遍历**](https://baike.baidu.com/item/先序遍历/6442839?fr=aladdin) 顺序相同。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

```
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [0]
输出：[0]
```

 

**提示：**

- 树中结点数在范围 `[0, 2000]` 内
- `-100 <= Node.val <= 100`

 

**进阶：**你可以使用原地算法（`O(1)` 额外空间）展开这棵树吗？

通过次数114,528 提交次数159,300



## 题解

>后序遍历：先拉平左右子树（递归完成），然后将左子树变为右子树，将旧右子树接到现右子树上
>
>**给** **`flatten`** **函数输入一个节点** **`root`****，那么以** **`root`** **为根的二叉树就会被拉平为一条链表**。
>
>我们再梳理一下，如何按题目要求把一棵树拉平成一条链表？很简单，以下流程：
>
>1. 将 `root` 的左子树和右子树拉平。
>2.  将 `root` 的右子树接到左子树下方，然后将整个左子树作为右子树。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def flatten_builder(root):
            if not root:
                return
            

            flatten_builder(root.left)
            flatten_builder(root.right)

            left = root.left
            right = root.right

            root.left = None
            root.right = left

            p = root
            while p.right:
                p = p.right
            p.right = right
        
        flatten_builder(root)
        return root
```

