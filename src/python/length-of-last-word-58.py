class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        strs = s.split(' ')
        if len(strs) == 0:
            return 0
        return len(strs[-1])
