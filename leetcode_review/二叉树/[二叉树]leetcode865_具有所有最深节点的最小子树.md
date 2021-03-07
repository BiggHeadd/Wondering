# [865. 具有所有最深节点的最小子树](https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

## 描述

难度中等

给定一个根为 `root` 的二叉树，每个节点的深度是 **该节点到根的最短距离** 。

如果一个节点在 **整个树** 的任意节点之间具有最大的深度，则该节点是 **最深的** 。

一个节点的 **子树** 是该节点加上它的所有后代的集合。

返回能满足 **以该节点为根的子树中包含所有最深的节点** 这一条件的具有最大深度的节点。

 

**注意：**本题与力扣 1123 重复：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/

 

**示例 1：**

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：
我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 5、3 和 2 包含树中最深的节点，但节点 2 的子树最小，因此我们返回它。
```

**示例 2：**

```
输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点。
```

**示例 3：**

```
输入：root = [0,1,3,null,2]
输出：[2]
解释：树中最深的节点为 2 ，有效子树为节点 2、1 和 0 的子树，但节点 2 的子树最小。
```

 

**提示：**

- 树中节点的数量介于 1 和 500 之间。
- `0 <= Node.val <= 500`
- 每个节点的值都是独一无二的。

通过次数6,209 提交次数9,889



## 题解

> **解读题意**：得到的子树**必须包含所有最深的结点且子树的总结点数最少**，然后返回这个子树的根节点。
>
> **后序遍历**二叉树的每个节点，得到左右子树的深度。
>
> 在递归函数中，对每个子树的处理分三种情况：
>
> 1. 如果 `左子树深度 == 右子树深度`，则返回当前节点；
> 2. 如果 `左子树深度 > 右子树深度`，返回左结点；
> 3. 如果 `左子树深度 < 右子树深度`，返回右深度。
>
> 最后，就能得到满足条件的那个根节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def max_depth(root):
            if not root:
                return 0
            
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            return max(left_depth, right_depth) + 1

        def finder(root):
            if not root:
                return None
            
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            if left_depth == right_depth:
                return root
            elif left_depth < right_depth:
                return finder(root.right)
            else:
                return finder(root.left)
        
        return finder(root)
```