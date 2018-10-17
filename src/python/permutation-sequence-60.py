import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n+1)]

        res = []
        k = k - 1  # 转换为下标

        for i in range(n - 1, -1, -1):
            nf = math.factorial(i)
            nk = int(k / nf)
            res.append(nums.pop(nk))
            k = k % nf

        return "".join(res)
