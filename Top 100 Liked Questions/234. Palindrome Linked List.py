# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 10 min, 	1200 ms	86.5 MB
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head:
            list.append(head.val)
            head = head.next

        if len(list) % 2 == 1:
            return False

        for i in range(int(len(list)/2)):
            if list[i] != list[-1-i]:
                return False
        return True
