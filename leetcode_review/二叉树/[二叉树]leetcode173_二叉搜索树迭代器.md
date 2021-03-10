# [173. 二叉搜索树迭代器](https://leetcode-cn.com/problems/binary-search-tree-iterator/)

## 描述

难度中等

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 `next()` 将返回二叉搜索树中的下一个最小的数。

 

**示例：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/25/bst-tree.png)**

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
```

 

**提示：**

- `next()` 和 `hasNext()` 操作的时间复杂度是 O(1)，并使用 O(*h*) 内存，其中 *h* 是树的高度。
- 你可以假设 `next()` 调用总是有效的，也就是说，当调用 `next()` 时，BST 中至少存在一个下一个最小的数。

通过次数38,762 提交次数50,995



## 题解

> 1. 中序遍历铺平二叉搜索树
> 2. 设置Pointer来实现next
> 3. 以point和二叉搜索树铺平后的长度来判断是否hasNext()

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.pointer = 0
        self.path = []
        def recursion(node):
            if not node:
                return

            recursion(node.left)
            self.path.append(node.val)
            recursion(node.right) 
        recursion(root)
        self.length = len(self.path)

    def next(self) -> int:
        num = self.path[self.pointer]
        self.pointer += 1
        return num

    def hasNext(self) -> bool:
        return self.pointer < self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```



> 算法：
>
> 初始化一个空栈 S，用于模拟二叉搜索树的中序遍历。中序遍历我们采用与之前相同的方法，只是我们现在使用的是自己的栈而不是系统的堆栈。由于我们使用自定义的数据结构，因此可以随时暂停和恢复递归。
> 我们还要实现一个帮助函数，在实现中将一次又一次的调用它。这个函数叫 _inorder_left，它将给定节点中的所有左子节点添加到栈中，直到节点没有左子节点为止。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._inorder_left(root)
    
    def _inorder_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node_tmp = self.stack.pop()
        if node_tmp.right:
            self._inorder_left(node_tmp.right)
        return node_tmp.val


    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

