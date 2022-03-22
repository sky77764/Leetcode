# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# sol, 1369 ms	16.3 MB
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        cur_diameter = self.getMaxDepth(root.left) + self.getMaxDepth(root.right)
        return max(cur_diameter, max(left, right))

    def getMaxDepth(self, root):
        if root is None:
            return 0

        return 1 + max(self.getMaxDepth(root.left), self.getMaxDepth(root.right))
