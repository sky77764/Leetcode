# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 15 min, 31 ms	13.6 MB
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new_root=None
        if root is not None:
            new_root = TreeNode(root.val)
            new_root.left = self.invertTree(root.right)
            new_root.right = self.invertTree(root.left)
        return new_root

