# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current_node = head
        count_node = 0

        while current_node and count_node != k:
            current_node = current_node.next
            count_node += 1

        if count_node == k:
            current_node = self.reverseKGroup(current_node, k)

            while count_node > 0:
                temp_node = head.next
                head.next = current_node
                current_node = head
                head = temp_node
                count_node -= 1
            head = current_node

        return head
