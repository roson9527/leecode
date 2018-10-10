# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_tmp = []
        for node in lists:
            while node:
                res_tmp.append(node.val)
                node = node.next

        res_tmp.sort()
        new_head = ListNode(0)
        rep = new_head
        for i in range(len(res_tmp)):
            rep.next = ListNode(res_tmp[i])
            rep = rep.next

        return new_head.next
