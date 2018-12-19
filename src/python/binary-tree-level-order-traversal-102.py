# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        stack = [root]  #
        yy = []
        k = 0  # 用于判断当前层是奇数层还是偶数层
        while stack:
            k += 1
            y = []
            l = len(stack)
            for i in range(l):
                cur = stack.pop(0)
                y.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)

            yy.append(y)
        return yy
