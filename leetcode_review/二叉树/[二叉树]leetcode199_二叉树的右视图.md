# [199. 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/)

## 描述

难度中等420收藏分享切换为英文接收动态反馈

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**示例:**

```
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

通过次数88,331 提交次数135,877



## 题解

> 树的层序遍历的进阶，遍历树的时候设置双指针，`pre`指向当前层的最后一个节点，`next`指向遍历到的最新的结点，取出每层最后一个结点(`pre`)的值到结果数组`res`。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        pre = root
        nxt = None
        result = []

        while queue:
            cur = queue.popleft()

            if cur.left:
                queue.append(cur.left)
                nxt = cur.left
            if cur.right:
                queue.append(cur.right)
                nxt = cur.right
            if cur == pre:
                result.append(cur.val)
                pre = nxt
        return result
```

