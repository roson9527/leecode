# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        return self.mergeSort(head)

    def mergeSort(self, head):
        if head.next == None:
            return head

        mid = head
        end = head
        pre = None
        while end and end.next:
            pre = mid
            mid = mid.next
            end = end.next.next

        if pre:
            pre.next = None
        l = self.mergeSort(head)
        r = self.mergeSort(mid)
        return self.merge(l, r)

    def merge(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy

        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next

            cur = cur.next

        if head1 != None:
            cur.next = head1
        if head2 != None:
            cur.next = head2

        return dummy.next
