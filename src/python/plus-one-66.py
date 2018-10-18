class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join([str(i) for i in digits])
        s = str(int(s) + 1)
        return [int(s[i]) for i in range(len(s))]
