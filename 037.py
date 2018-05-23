class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solveRec(board)

    def solveRec(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        c = chr(ord('0')+num)
                        if self.isvalid(board, i, j, c):
                            board[i][j] = c
                            if self.solveRec(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True




    def isvalid(self, board, row, column, c):
        for i in range(len(board)):
            if board[i][column]!='.' and board[i][column] == c:
                return False
            if board[row][i]!='.' and board[row][i] == c:
                return False
            if board[int(row/3)*3 +int(i/3)][int(column/3)*3+int(i%3)]!='.' and board[int(row/3)*3 +int(i/3)][int(column/3)*3+int(i%3)] == c:
                return False
        return True

if __name__=="__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solu = Solution()
    solu.solveSudoku(board)
    print(board)