# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 30 min, 23 ms	13.3 MB
class Solution(object):
    def inorderTraversal(self, root, output=[], init=True):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if init:
            output = []
        if root is not None:
            self.inorderTraversal(root.left, output=output, init=False)
            output.append(root.val)
            self.inorderTraversal(root.right, output=output, init=False)

        return output

# sol, 32 ms	13.4 MB
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        output = []

        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left
            output.append(stack[-1].val)
            root = stack[-1].right
            stack = stack[:-1]

        return output


