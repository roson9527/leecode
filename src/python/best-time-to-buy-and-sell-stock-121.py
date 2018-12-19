class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        minn = prices[0]
        maxn = minn
        sums = 0
        for i in range(1, len(prices)):
            p = prices[i]
            if p < minn:
                minn = p
                maxn = p
            else:
                maxn = max(p, maxn)
                sums = max(maxn - minn, sums)

        return sums
