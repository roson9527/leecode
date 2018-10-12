class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:  # 类似于斐波拉契数，后面的数跟前面的数有关
            return '1'
        if n == 2:
            return '11'

        pre = '11'
        for _ in range(3, n+1):
            res = ''
            cnt = 1

            length = len(pre)
            for j in range(1, length):
                if pre[j-1] == pre[j]:
                    cnt += 1
                else:
                    res += str(cnt)+pre[j-1]
                    cnt = 1
            res += str(cnt)+pre[j]
            pre = res

        return res
