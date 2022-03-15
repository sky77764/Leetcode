# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 3min, 36 ms	16.9 MB
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev_node = None
        while head:
            cur_node = ListNode(head.val, next=prev_node)
            prev_node = cur_node
            head = head.next


