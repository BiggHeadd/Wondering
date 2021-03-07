# [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## 描述

难度中等

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/最近公共祖先/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
```

**示例 3：**

```
输入：root = [1,2], p = 1, q = 2
输出：1
```

 

**提示：**

- 树中节点数目在范围 `[2, 105]` 内。
- `-109 <= Node.val <= 109`
- 所有 `Node.val` `互不相同` 。
- `p != q`
- `p` 和 `q` 均存在于给定的二叉树中。

通过次数165,317 提交次数248,460



## 题解

> #### 方法1
>
> 分为以下几个步骤：
>
> 1. 找到从根到p指向结点的路径，并存储在一个向量或数组中；
> 2. 找到从根到q指向结点的路径，并存储在一个向量或数组中；
> 3. **同时**从这两条路径起点开始走，直到**遇到一个不同的节点**，则**它前面的那个**即为`p`,`q`的最近公共祖先。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        def find_path(root, target, path):
            if not root:
                return False
            
            if root == target:
                path.append(root)
                return True

            path.append(root)
            left = find_path(root.left, target, path)
            right = find_path(root.right, target, path)
            
            if left or right:
                return True
            
            path.pop()
            return False

        path_p, path_q = [], []
        find_path(root, p, path_p)
        find_path(root, q, path_q)

        i = 0
        while i < len(path_p) and i < len(path_q):
            if path_p[i] != path_q[i]:
                break
            i += 1

        if i == len(path_p):
            return path_p[-1]
        if i == len(path_q):
            return path_q[-1]
        return path_p[i-1]
```



> #### 方法2
>
> 从根节点开始遍历二叉树，对二叉树的每一个子树（包括整个树），设它的根节点为`root`如果`node1`和`node2`中的任一个和`root`匹配，那么`root`就是最低公共祖先。 如果都不匹配，则分别递归左、右子树，如果有一个 节点出现在左子树，并且另一个节点出现在右子树，则`root`就是最近公共祖先.  如果两个节点都出现在左子树，则说明最低公共祖先在左子树中，否则在右子树。
>
> 具体过程：后序遍历二叉树，对每个子树，有以下几种情况：
>
> 1. 当前节点为空，返回`nullptr`；
> 2. 当前节点在`p`,`q`两节点之间，返回相等的那个；
> 3. 以上条件都不符合，得到左右子树后序遍历的结果`lp`和`rp`：
>    * 如果`lp`和`rp`都是非空，则返回当前节点（当前节点就是最近祖先） ；
>    * `lp`和`rp`有一个为空，返回`lp`,`rp`中非空的那个。
>
> 最后，当遍历完整个二叉树，得到的就是p,q节点的最近公共祖先。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        def finder(root):
            if not root:
                return None
            if root == p:
                return p
            if root == q:
                return q
            
            l = finder(root.left)
            r = finder(root.right)

            if not l and not r:
                return None
            if not l:
                return r
            if not r:
                return l
            return root
        return finder(root)
```

