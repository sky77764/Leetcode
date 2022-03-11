# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 10 min, 64 ms	20.6 MB
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        max_num = 10000
        cnt = 0
        while head is not None:
            if head.next is None:
                return False
            elif cnt > max_num:
                return True
            else:
                head = head.next
                cnt += 1
        return False

