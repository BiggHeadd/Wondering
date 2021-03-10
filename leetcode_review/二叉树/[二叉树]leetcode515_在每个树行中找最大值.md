# [515. 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)

## 描述

难度中等

您需要在二叉树的每一行中找到最大的值。

**示例：**

```
输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]
```

通过次数25,667 提交次数40,337



## 题解

> 层次遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        ans = []
        while len(queue) > 0:
            length = len(queue)

            biggest = float('-inf')
            for _ in range(length):
                node = queue.popleft()

                biggest = max(biggest, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(biggest)
        return ans
```

