# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        p_head = head
        while p_head:
            p_head_next = p_head.next
            p_head.next = last
            last = p_head
            p_head = p_head_next

        return last
