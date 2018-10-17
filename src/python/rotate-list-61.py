# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head == None:
            return head

        old_head = head
        pre = old_head
        cnt = 1
        while pre != None and pre.next != None:
            pre = pre.next
            cnt += 1

        k = cnt - k % cnt
        if k == 0:
            return old_head

        pre.next = old_head
        cur = old_head
        new_head = None
        for i in range(1, k+1):
            if i == k:
                new_head = cur.next
                cur.next = None
                break
            else:
                cur = cur.next

        return new_head
