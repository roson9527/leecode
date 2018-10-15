class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = map(list,zip(*matrix[::-1]))
        length = len(matrix)
        for i in range(length):
            for j in range(i+1, length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
