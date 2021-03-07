# [103. 二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

## 描述

难度中等

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回锯齿形层序遍历如下：

```
[
  [3],
  [20,9],
  [15,7]
]
```

通过次数118,083 提交次数206,764



## 题解

> 双指针法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([root])
        pre = root
        nxt = None
        tmp = []
        flag = True
        ans = []

        while queue:
            cur = queue.popleft()
            tmp.append(cur.val)

            if cur.left:
                queue.append(cur.left)
                nxt = cur.left
            if cur.right:
                queue.append(cur.right)
                nxt = cur.right
            if cur == pre:
                pre = nxt

                if not flag:
                    tmp.reverse()
                ans.append(tmp)
                tmp = []
                flag = not flag
        return ans
```



> bfs

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = []
        queue.append(root)
        depth = 0

        while len(queue) > 0:
            length = len(queue)
            tmp = []
            depth += 1

            for i in range(length):
                node = queue.pop(0)

                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if len(tmp) > 0:
                if depth % 2 == 0:
                    tmp.reverse()
                    ans.append(tmp)
                else:
                    ans.append(tmp)

        return ans
```

