# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# sol, 196 ms	43.5 MB
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = set()

        while headA:
            visited.add(headA)
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            headB = headB.next

        return None
