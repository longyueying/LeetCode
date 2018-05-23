class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [['.']*n for _ in range(n)]
        self.solve(board, 0, res)
        return len(res)

    def solve(self, board, row, res):

        if row >= len(board):
            temp = []
            for l in board:
                temp.append(''.join(l))
            res.append(temp)
        else:
            for j in range(len(board)):
                if self.isValid(board, row, j):
                    board[row][j] = 'Q'
                    self.solve(board, row+1, res)
                    board[row][j] = '.'


    def isValid(self, board, row, column):
        for i in range(len(board)):
            if board[row][i] == 'Q':
                return False
            if board[i][column] == 'Q':
                return False
            if column + (row-i)>=0 and column + (row-i) <len(board):
                if board[i][column + (row-i)] == 'Q':
                    return False
            if column - (row-i)>=0 and column - (row-i) <len(board):
                if board[i][column - (row-i)] == 'Q':
                    return False
        return True

if __name__=="__main__":
    solu = Solution()
    print(solu.totalNQueens(4))