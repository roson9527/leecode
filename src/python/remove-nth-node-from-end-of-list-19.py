class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        offset_node = head
        for _ in range(n):
            offset_node = offset_node.next

        # remove head
        if offset_node == None:
            return head.next

        frist_node = head
        while offset_node.next != None:
            offset_node = offset_node.next
            frist_node = frist_node.next

        frist_node.next = frist_node.next.next
        return head
