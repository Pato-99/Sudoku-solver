class SudokuSolver:
    def __init__(self, board=None):
        if not board:
            self.board = [[0 for i in range(9)] for j in range(9)]
        else:
            self.board = board

    def __str__(self):
        string = ""
        for i in range(9):
            if i > 0 and i % 3 == 0:
                string += 6 * "-" + "|" + 7 * "-" + "|" + 6 * "-" + "\n"
            for j in range(9):
                if j > 0 and j % 3 == 0:
                    string += "| "
                if self.board[i][j] == 0:
                    string += "_"
                else:
                    string += f"{self.board[i][j]}"
                if j < 8:
                    string += " "
            string += "\n"
        return string

    def check_if_possible(self, value, row, col):
        # check if free
        if self.board[row][col] != 0:
            return False

        # check row and column
        for i in range(9):
            if self.board[i][col] == value:
                return False
            if self.board[row][i] == value:
                return False

        # check chunk
        # 0-2 | 3-5 | 6-8
        chunk_row = row // 3
        chunk_col = col // 3

        row_start = chunk_row * 3
        row_end = row_start + 3

        col_start = chunk_col * 3
        col_end = col_start + 3

        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                if self.board[i][j] == value:
                    return False
        return True

    def validate_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    continue
                tmp = self.board[i][j]
                self.board[i][j] = 0
                if not self.check_if_possible(tmp, i, j):
                    self.board[i][j] = tmp
                    return False
                self.board[i][j] = tmp
        return True

    def solve(self, i=0, j=0):
        if i > 8:
            return True

        if self.board[i][j] != 0:
            if j == 8:
                if self.solve(i + 1, 0):
                    return True
            else:
                if self.solve(i, j + 1):
                    return True

        for k in range(1, 10):
            if self.check_if_possible(k, i, j):
                self.board[i][j] = k

                if j == 8:
                    if self.solve(i + 1, 0):
                        return True
                else:
                    if self.solve(i, j + 1):
                        return True

                self.board[i][j] = 0

        return False
