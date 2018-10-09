class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1 or len(s) == 0:
            return False

        check = {')': '(', ']': '[', '}': '{'}
        l = [None]
        for i in s:
            if i in check and check[i] == l[-1]:
                l.pop()
            else:
                l.append(i)

        return len(l) == 1
