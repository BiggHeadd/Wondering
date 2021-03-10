# [501. 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)

## 描述

难度简单

给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

- 结点左子树中所含结点的值小于等于当前结点的值
- 结点右子树中所含结点的值大于等于当前结点的值
- 左子树和右子树都是二叉搜索树

例如：
给定 BST `[1,null,2,2]`,

```
   1
    \
     2
    /
   2
```

`返回[2]`.

**提示**：如果众数超过1个，不需考虑输出顺序

**进阶：**你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

通过次数48,921 提交次数97,729



## 题解

> #### Morris 中序遍历
>
> - 如果当前节点没有左子树，则遍历这个点，然后跳转到当前节点的右子树。
> - 如果当前节点有左子树，那么它的前驱节点一定在左子树上，我们可以在左子树上一直向右行走，找到当前点的前驱节点。
>   - 如果前驱节点没有右子树，就将前驱节点的 \textit{right}right 指针指向当前节点。这一步是为了在遍历完前驱节点后能找到前驱节点的后继，也就是当前节点。
>   - 如果前驱节点的右子树为当前节点，说明前驱节点已经被遍历过并被修改了 \textit{right}right 指针，这个时候我们重新将前驱的右孩子设置为空，遍历当前的点，然后跳转到当前节点的右子树。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        base = 0
        count = 0
        max_count = 1

        def update(value):
            nonlocal base, ans, count, max_count
            if base == value:
                count += 1
            else:
                base = value
                count = 1
            
            if count == max_count:
                ans.append(value)
            if count > max_count:
                max_count = count
                ans = [value]

        def builder(node):
            while node:
                if not node.left:
                    update(node.val)
                    node = node.right
                    continue
                
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = node
                    node = node.left
                else:
                    pre.right = None
                    update(node.val)
                    node = node.right
        
        builder(root)
        return ans
```

