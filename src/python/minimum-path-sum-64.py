class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)

        if m == 1:
            return sum(g[0] for g in grid)
        if n == 1:
            return sum(grid[0])

        # 横
        for i in range(1, m):
            grid[0][i] = grid[0][i] + grid[0][i - 1]

        # 竖
        for i in range(1, n):
            grid[i][0] = grid[i][0] + grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                from_left = grid[j][i] + grid[j][i-1]
                from_up = grid[j][i] + grid[j-1][i]
                grid[j][i] = min(from_left, from_up)

        return grid[-1][-1]
