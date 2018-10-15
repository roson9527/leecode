class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # print(x, n)
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 1:
            return self.myPow(x*x, int(n/2)) * x
        else:
            return self.myPow(x*x, int(n/2))
