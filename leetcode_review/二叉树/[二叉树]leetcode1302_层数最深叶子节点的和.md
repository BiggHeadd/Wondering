# [1302. 层数最深叶子节点的和](https://leetcode-cn.com/problems/deepest-leaves-sum/)

## 描述

难度中等

给你一棵二叉树，请你返回层数最深的叶子节点的和。

 

**示例：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/28/1483_ex1.png)**

```
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
```

 

**提示：**

- 树中节点数目在 `1` 到 `10^4` 之间。
- 每个节点的值在 `1` 到 `100` 之间。

通过次数14,309 提交次数17,587



## 题解

> 前序遍历
>
> 1. 维护全局变量total和max_depth
> 2. 当前深度 > max_depth，total重置
> 3. 当前深度 = max_depth，total累加

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_depth = 0
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:

        def recursion(node, depth):
            if not node:
                return None

            if not node.left and not node.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.total = node.val
                elif depth == self.max_depth:
                    self.total += node.val
                
            recursion(node.left, depth+1)
            recursion(node.right, depth+1)
        
        recursion(root, 0)
        return self.total
```



> 层次遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        
        while len(queue) > 0:
            length = len(queue)

            tmp = 0
            for _ in range(length):
                node = queue.popleft()

                tmp += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return tmp
```

