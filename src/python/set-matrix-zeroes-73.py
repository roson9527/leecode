class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        x_zero = False
        y_zero = False
        if 0 in matrix[0]:
            x_zero = True

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                y_zero = True
                break

        for i in range(1, len(matrix)):
            flag = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    flag = True

            if flag:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        if x_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if y_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
