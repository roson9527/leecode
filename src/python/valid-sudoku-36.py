class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # line
        for line in board:
            if not self.validGroup(line):
                return False

        for i in range(9):
            tmp_group = [board[k][i] for k in range(9)]
            # print(tmp_group)
            if not self.validGroup(tmp_group):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp_group = []
                for offset in range(3):
                    tmp_group.extend([board[i+offset][j+k] for k in range(3)])
                if not self.validGroup(tmp_group):
                    return False

        return True

    def validGroup(self, sd_group=None):
        set_group = [i for i in set(sd_group) if i != '.']
        count = [sd_group.count(key)
                 for key in set_group if sd_group.count(key) > 1]
        if len(count) > 0:
            return False

        return True
