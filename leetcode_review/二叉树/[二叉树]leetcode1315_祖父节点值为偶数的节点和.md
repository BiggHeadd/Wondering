# [1315. 祖父节点值为偶数的节点和](https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/)

## 描述

难度中等

给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

- 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）

如果不存在祖父节点值为偶数的节点，那么返回 `0` 。

 

**示例：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/10/1473_ex1.png)**

```
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
```

 

**提示：**

- 树中节点的数目在 `1` 到 `10^4` 之间。
- 每个节点的值在 `1` 到 `100` 之间。

通过次数10,252 提交次数12,647



## 题解

> 前序遍历dfs

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        ans = 0

        def dfs(grandfather, father, son):
            if not son:
                return
            
            if grandfather % 2 == 0:
                nonlocal ans
                ans += son.val
            
            dfs(father, son.val, son.left)
            dfs(father, son.val, son.right)
        
        dfs(1, 1, root)
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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        ans = 0

        while len(queue) > 0:
            node = queue.popleft()

            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
```

