class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        num_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        num_roman = ["M", "CM", "D", "CD", "C", "XC",
                     "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ""

        for i in range(len(num_val)):
            while num >= num_val[i]:
                num -= num_val[i]
                res += num_roman[i]

        return res
