# [1305. 两棵二叉搜索树中的所有元素](https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/)

## 描述

难度中等

给你 `root1` 和 `root2` 这两棵二叉搜索树。

请你返回一个列表，其中包含 **两棵树** 中的所有整数并按 **升序** 排序。.

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/29/q2-e1.png)

```
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
```

**示例 2：**

```
输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]
```

**示例 3：**

```
输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]
```

**示例 4：**

```
输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]
```

**示例 5：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/29/q2-e5-.png)

```
输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
```

 

**提示：**

- 每棵树最多有 `5000` 个节点。
- 每个节点的值在 `[-10^5, 10^5]` 之间。

通过次数11,723 提交次数15,764



## 题解

> 中序遍历铺平+归并排序

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return []
        
        root1_stack = []
        root2_stack = []

        def recursion(node, stack):
            if not node:
                return
            
            recursion(node.left, stack)
            stack.append(node.val)
            recursion(node.right, stack)

        recursion(root1, root1_stack)
        recursion(root2, root2_stack)
        
        ans = []
        i = j = 0
        while i < len(root1_stack) and j < len(root2_stack):
            if root1_stack[i] < root2_stack[j]:
                ans.append(root1_stack[i])
                i += 1
            else:
                ans.append(root2_stack[j])
                j += 1
        if i == len(root1_stack):
            for num in root2_stack[j:]:
                ans.append(num)
        elif j == len(root2_stack):
            for num in root1_stack[i:]:
                ans.append(num)
        return ans
```

