class Cache:
    def __init__(self, x, y, cache):
        self.x = x
        self.y = y
        self.cache = cache
        self.indx = 0


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        src_list = self.buildCache(board)
        cur = 0
        while cur < len(src_list):
            num = self.get_cache_num(src_list, cur)
            if num == -1:
                self.rollBack(board, src_list, cur)
                cur -= 1
                continue

            c = src_list[cur]
            board[c.y][c.x] = num
            #print(board)
            if self.isValidSudoku(board):
                #print(board)
                cur += 1
            #else:
                #board[c.y][c.x] = '.'

    def rollBack(self, board, src_list, n):
        c = src_list[n]
        board[c.y][c.x] = '.'
        src_list[n].indx = 0

    def get_cache_num(self, src_list, n):
        c = src_list[n]
        if c.indx == len(c.cache):
            return -1
        num = c.cache[c.indx]
        src_list[n].indx += 1
        return num

    def buildCache(self, board):
        src_list = []
        core_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for indx in range(81):
            x = indx % 9
            y = int(indx / 9)

            if board[y][x] == '.':
                # 找差集
                # 横
                horizon = set(board[y])
                vertical = set([board[i][x] for i in range(9)])
                # 组
                g_x = int(x / 3) * 3
                g_y = int(y / 3) * 3
                tmp_group = []
                for offset in range(3):
                    tmp_group.extend([board[g_y+offset][g_x+k]
                                      for k in range(3)])
                tmp_group = set(tmp_group)

                # 备选的数字
                cache_num = set(core_num).difference(
                    tmp_group.union(horizon).union(vertical))
                if len(cache_num) == 1:
                    board[y][x] = list(cache_num)[0]
                else:
                    src_list.append(Cache(x, y, list(cache_num)))

                # print("x:", x, "y:", y, "cache:", cache_num)

        return src_list

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