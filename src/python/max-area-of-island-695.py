class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                max_area = max(self.dfs(grid, x, y), max_area)

        return max_area

    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == 0:
            return 0

        grid[y][x] = 0
        ret = self.dfs(grid, x, y-1) + self.dfs(grid, x, y+1) + \
            self.dfs(grid, x+1, y) + self.dfs(grid, x-1, y)
        return ret + 1
