class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        maps = [-1 for _ in range(len(M))]
        for y in range(len(M)):
            for x in range(len(M[0])):
                if x != y and M[y][x] == 1:
                    y_point = self.findRoot(maps, y)
                    x_point = self.findRoot(maps, x)
                    if y_point != x_point:
                        maps[y_point] = x_point

        return maps.count(-1)

    def findRoot(self, maps, y):
        if maps[y] == -1:
            return y

        return self.findRoot(maps, maps[y])
