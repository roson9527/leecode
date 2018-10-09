class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0

        for i in range(len(s)):
            c = s[i]
            if c == "I":
                sum += 1
            elif c == "V":
                sum += 5
            elif c == "X":
                sum += 10
            elif c == "L":
                sum += 50
            elif c == "C":
                sum += 100
            elif c == "D":
                sum += 500
            elif c == "M":
                sum += 1000

            if i < 1:
                continue

            if c == "V" or c == "X":
                if s[i-1] == "I":
                    sum -= 2
            elif c == "L" or c == "C":
                if s[i-1] == "X":
                    sum -= 20
            elif c == "D" or c == "M":
                if s[i-1] == "C":
                    sum -= 200

        return sum
