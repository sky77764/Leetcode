# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 35min,	24 ms	13.7 MB
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_list = self.leftTraversal(root.left)
        right_list = self.rightTraversal(root.right)

        if len(left_list) != len(right_list):
            return False

        for i in range(len(left_list)):
            if left_list[i] != right_list[i]:
                return False

        return True

    def leftTraversal(self, root, output=[], init=True):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if init:
            output = []
        if root is not None:
            output.append(root.val)
            self.leftTraversal(root.left, output=output, init=False)
            self.leftTraversal(root.right, output=output, init=False)
        else:
            output.append(None)

        return output

    def rightTraversal(self, root, output=[], init=True):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if init:
            output = []
        if root is not None:
            output.append(root.val)
            self.rightTraversal(root.right, output=output, init=False)
            self.rightTraversal(root.left, output=output, init=False)
        else:
            output.append(None)

        return output