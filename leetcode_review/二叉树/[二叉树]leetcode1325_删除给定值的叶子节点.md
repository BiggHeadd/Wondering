# [1325. 删除给定值的叶子节点](https://leetcode-cn.com/problems/delete-leaves-with-a-given-value/)

## 描述

难度中等

给你一棵以 `root` 为根的二叉树和一个整数 `target` ，请你删除所有值为 `target` 的 **叶子节点** 。

注意，一旦删除值为 `target` 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 `target` ，那么这个节点也应该被删除。

也就是说，你需要重复此过程直到不能继续删除。

 

**示例 1：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/16/sample_1_1684.png)**

```
输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：
上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。
```

**示例 2：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/16/sample_2_1684.png)**

```
输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]
```

**示例 3：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/16/sample_3_1684.png)**

```
输入：root = [1,2,null,2,null,2], target = 2
输出：[1]
解释：每一步都删除一个绿色的叶子节点（值为 2）。
```

**示例 4：**

```
输入：root = [1,1,1], target = 1
输出：[]
```

**示例 5：**

```
输入：root = [1,2,3], target = 1
输出：[1,2,3]
```

 

**提示：**

- `1 <= target <= 1000`
- 每一棵树最多有 `3000` 个节点。
- 每一个节点值的范围是 `[1, 1000]` 。

通过次数7,472 提交次数10,213



## 题解

> 具体地，当我们回溯到某个节点 u 时，如果 u 的左右孩子均不存在（这里有两种情况，一是节点 u 的孩子本来就不存在，二是节点 u 的孩子变成了叶子节点并且值为 target，导致其被删除），并且值为 target，那么我们要删除节点 u，递归函数的返回值为空节点；如果节点 u 不需要被删除，那么递归函数的返回值为节点 u 本身。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        
        def recursion(node, target):
            if not node:
                return None
            
            node.left = recursion(node.left, target)
            node.right = recursion(node.right, target)

            if not node.left and not node.right and node.val == target:
                return None
            return node
        return recursion(root, target)
```

