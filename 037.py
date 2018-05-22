class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solveRec(board, 0)

    def solveRec(self, board, index):
        if index == len(board)*len(board):
            return True


    def isvalid(self, board, row, column):
        for i in range(len(board)):
            if board[i][column] == board[row][column] and row != i:
                return False
        for j in range(len(board)):
            if board[row][j] == board[row][column] and column!=j:
                return False

        for i in range(int(row/3) * 3, int(row/3) * 3+3):
            for j in range(int(column/3)*3, int(column/3)*3+3):
                if board[i][j] == board[row][column] and (not (row==i and column==j)):
                    return False
        return True