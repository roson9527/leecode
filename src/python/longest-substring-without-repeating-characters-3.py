class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxl = 0
        
        for x in s:
            if x not in stack:
                stack.append(x)
            else:
                i = stack.index(x)
                stack = stack[i+1:]
                stack.append(x)
            maxl = max(len(stack), maxl)

        return maxl
