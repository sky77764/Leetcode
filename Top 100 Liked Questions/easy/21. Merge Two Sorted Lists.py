# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 35min, 32 ms	13.6 MB, ListNode 안쓰려다가 오히려 코드 복잡해짐.
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1_, list2_ = [], []
        while True:
            if list1 is None:
                break
            list1_.append(list1.val)
            list1 = list1.next
        while True:
            if list2 is None:
                break
            list2_.append(list2.val)
            list2 = list2.next

        list1 = list1_
        list2 = list2_

        merged_list = []
        j = 0
        while len(list1) > 0:
            if j >= len(list2):
                merged_list.append(list1[0])
                list1 = list1[1:]
            else:
                if list1[0] <= list2[0]:
                    merged_list.append(list1[0])
                    if len(list1) == 1:
                        list1 = []
                    else:
                        list1 = list1[1:]
                else:
                    merged_list.append(list2[0])
                    if len(list2) == 1:
                        list2 = []
                    else:
                        list2 = list2[1:]

        while len(list2) > 0:
            merged_list.append(list2[0])
            if len(list2) == 1:
                list2 = []
            else:
                list2 = list2[1:]

        merged_list_node, head = None, None
        for item in merged_list:
            if merged_list_node is None:
                merged_list_node = ListNode(val=item, next=None)
                head = merged_list_node
            else:
                merged_list_node.next = ListNode(val=item, next=None)
                merged_list_node = merged_list_node.next
        return head


if __name__ == '__main__':
    list1 = []
    list2 = [0]

    sol = Solution()
    print(sol.mergeTwoLists(list1, list2))