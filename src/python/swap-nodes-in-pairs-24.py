# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # tmp head
        new_head = ListNode(0)
        new_head.next = head

        rep = new_head

        while rep.next and rep.next.next:
            j = rep.next
            q = rep.next.next

            j.next = q.next
            rep.next = q
            q.next = j

            rep = rep.next.next

        return new_head.next
