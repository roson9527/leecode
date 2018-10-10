class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        left = n
        right = n
        string = ""
        self.generate(left, right, string, res)
        return res

    def generate(self, left, right, string, res):
        if left > 0:
            self.generate(left - 1, right, string + "(", res)
        if left < right and right > 0:
            self.generate(left, right - 1, string + ")", res)
        if left == 0 and right == 0:
            res.append(string)
