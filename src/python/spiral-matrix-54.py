class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        self.ans = []
        self.lines(matrix, 0, 0, len(matrix[0])-1, len(matrix)-1)
        return self.ans

    # 打印一圈
    def lines(self, matrix, start_x, start_y, end_x, end_y):
        #print(start_x, start_y, end_x, end_y)
        if start_x > end_x or start_y > end_y:
            return
        if end_y < 0 or end_x < 0:
            return
        # 1
        for i in range(start_x, end_x + 1):
            self.ans.append(matrix[start_y][i])
        #print("1:", self.ans)
        # 2
        for i in range(start_y + 1, end_y + 1):
            self.ans.append(matrix[i][end_x])
        #print("2:", self.ans)
        # 3
        if start_y != end_y:
            for i in range(end_x - 1, start_x - 1, -1):
                self.ans.append(matrix[end_y][i])
        #print("3:", self.ans)
        # 4
        if start_x != end_x:
            for i in range(end_y - 1, start_y, -1):
                self.ans.append(matrix[i][start_x])
        #print("4:", self.ans)

        self.lines(matrix, start_x+1, start_y+1, end_x-1, end_y-1)
