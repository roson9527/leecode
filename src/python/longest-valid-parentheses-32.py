class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tl = len(s)
        start_p = 0
        stack = []
        max_len = 0

        for i in range(tl):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start_p = i + 1
                    continue
                else:
                    a = stack.pop()
                    if len(stack) == 0:
                        max_len = max(i - start_p + 1, max_len)
                    else:
                        max_len = max(i - stack[-1], max_len)

        return max_len
