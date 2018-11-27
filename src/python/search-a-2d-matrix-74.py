class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        begin = 0
        end = len(matrix[0]) - 1

        if end < 0:
            return False

        for i in range(len(matrix)):
            m = matrix[i]
            if not (target >= m[begin] and target <= m[end]):
                continue

            if target in m:
                return True

        return False
