class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        if (m == 1 and ([1] in obstacleGrid)):
            return 0
        if (n == 1 and (1 in obstacleGrid[0])):
            return 0
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1

        # 行
        m_flag = True
        for i in range(1, m):
            if obstacleGrid[0][i] == 1:
                m_flag = False
            if m_flag:
                dp[0][i] = 1
            else:
                dp[0][i] = 0

        # 列
        n_flag = True
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                n_flag = False
            if n_flag:
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                left = dp[i-1][j] if obstacleGrid[i-1][j] != 1 else 0
                up = dp[i][j-1] if obstacleGrid[i][j-1] != 1 else 0
                # left + up
                dp[i][j] = left + up

        return dp[-1][-1]
