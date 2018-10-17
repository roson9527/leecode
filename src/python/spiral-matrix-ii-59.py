class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        total = n * n
        res = [[0]*n for _ in range(n)]

        row_beg = 0
        row_end = n - 1
        col_beg = 0
        col_end = n - 1

        while num <= total:
            for i in range(col_beg, col_end + 1):
                res[row_beg][i] = num
                num += 1

            row_beg += 1
            for i in range(row_beg, row_end + 1):
                res[i][col_end] = num
                num += 1

            col_end -= 1
            for i in range(col_end, col_beg - 1, -1):
                res[row_end][i] = num
                num += 1

            row_end -= 1
            for i in range(row_end, row_beg - 1, -1):
                res[i][col_beg] = num
                num += 1

            col_beg += 1

        return res
