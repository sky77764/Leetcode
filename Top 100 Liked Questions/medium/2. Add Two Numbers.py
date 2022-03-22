# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 20 min, 46 ms	13.4 MB
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        up = 0
        out = None
        out_list = []
        while l1 or l2 or up != 0:
            cur_sum = 0
            if l1:
                cur_sum += l1.val
                l1 = l1.next
            if l2:
                cur_sum += l2.val
                l2 = l2.next
            cur_sum += up
            up = 0

            if cur_sum >= 10:
                up = 1
                cur_sum -= 10

            out_list.append(cur_sum)

        if len(out_list) > 0:
            out = ListNode(val=out_list[-1])
        for i in range(len(out_list) - 2, -1, -1):
            cur_node = ListNode(val=out_list[i], next=out)
            out = cur_node
        return out