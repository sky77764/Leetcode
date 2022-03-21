# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 10 min, 111 ms	15.1 MB
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None and root2 is None:
            return None

        elif root1 is None:
            val = root2.val
            root1_left, root1_right = None, None
            root2_left, root2_right = root2.left, root2.right
        elif root2 is None:
            val = root1.val
            root1_left, root1_right = root1.left, root1.right
            root2_left, root2_right = None, None
        else:
            val = root1.val + root2.val
            root1_left, root1_right = root1.left, root1.right
            root2_left, root2_right = root2.left, root2.right

        return TreeNode(val = val, left = self.mergeTrees(root1_left, root2_left), right=self.mergeTrees(root1_right, root2_right))