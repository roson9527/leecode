class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = [["."]*n for _ in range(n)]
        self.ans = []
        self.dfs(queens, 0)
        return self.ans

    def check(self, queens, x, y):
        line = queens[y]
        if "Q" in line:
            return False
        for i in range(y):
            l = queens[i]
            pos = l.index("Q")
            if l[x] == "Q" or abs(pos - x) == abs(y - i):
                return False

        return True

    def dfs(self, queens, indx_y):
        if indx_y == len(queens):
            res = ["".join(raw) for raw in queens]
            self.ans.append(res)
            return True

        x = 0
        while x < len(queens):

            if self.check(queens, x, indx_y):
                queens[indx_y][x] = "Q"
                self.dfs(queens, indx_y + 1)
                queens[indx_y][x] = "."
            x += 1
