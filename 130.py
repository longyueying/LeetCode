from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        queue = deque()
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    queue.append((i,j))
                    board[i][j] = 'S'
        for j in [0, len(board[0])-1]:
            for i in range(len(board)):
                if board[i][j]=='O':
                    queue.append((i, j))
                    board[i][j] = 'S'

        while queue:
            k, q = queue.popleft()
            board[k][q] = 'S'
            if k - 1 > 0 and board[k - 1][q] == 'O':
                queue.append((k - 1, q))
            if q - 1 > 0 and board[k][q - 1] == "O":
                queue.append((k, q - 1))
            if k + 1 < len(board) and board[k + 1][q] == 'O':
                queue.append((k + 1, q))
            if q + 1 < len(board[0]) and board[k][q + 1] == 'O':
                queue.append((k, q + 1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    board[i][j]='O'
                else:
                    board[i][j] = 'X'


if __name__=="__main__":
    b = [["X","O","O","X","X","X","O","X","X","O","O","O","O","O","O","O","O","O","O","O"],
         ["X","O","O","X","X","O","O","X","O","O","O","X","O","X","O","X","O","O","X","O"],["O","O","O","X","X","X","X","O","X","O","X","X","O","O","O","O","X","O","X","O"],["O","O","O","X","X","O","O","X","O","O","O","X","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","X","X","X","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","X","O","X","X","O","O","O","O","O","O","X","O","X"],["O","O","O","X","O","O","O","X","O","X","O","X","O","X","O","X","O","X","O","X"],["O","O","O","X","O","X","O","O","X","X","O","X","O","X","X","O","X","X","X","O"],["O","O","O","O","X","O","O","X","X","O","O","O","O","X","O","O","O","X","O","X"],["O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O","X","O"],["X","O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O"],["O","X","O","O","O","X","O","X","O","X","X","O","X","X","X","O","X","X","O","O"],["X","X","O","X","O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","X"],["O","X","O","O","X","X","X","O","O","O","X","X","X","X","X","O","X","O","O","O"],["O","O","X","X","X","O","O","O","X","X","O","O","O","X","O","X","O","O","O","O"],["X","O","O","X","O","X","O","O","O","O","X","O","O","O","X","O","X","O","X","X"],["X","O","X","O","O","O","O","O","O","X","O","O","O","X","O","X","O","O","O","O"],["O","X","X","O","O","O","X","X","X","O","X","O","X","O","X","X","X","X","O","O"],["O","X","O","O","O","O","X","X","O","O","X","O","X","O","O","X","O","O","X","X"],["O","O","O","O","O","O","X","X","X","X","O","X","O","O","O","X","X","O","O","O"]]
    t = [["X","O","O","X","X","X","O","X","X","O","O","O","O","O","O","O","O","O","O","O"],
         ["X","O","O","X","X","O","O","X","O","O","O","X","O","X","O","X","O","O","X","O"],["O","O","O","X","X","X","X","X","X","O","X","X","O","O","O","O","X","O","X","O"],["O","O","O","X","X","O","O","X","O","O","O","X","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","X","X","X","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","X","X","X","X","O","O","O","O","O","O","X","O","X"],["O","O","O","X","O","O","O","X","X","X","O","X","O","X","O","X","O","X","O","X"],["O","O","O","X","O","X","O","O","X","X","O","X","O","X","X","X","X","X","X","O"],["O","O","O","O","X","O","O","X","X","O","O","O","O","X","X","X","X","X","X","X"],["O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","X","X","X","X","O"],["X","O","O","X","O","O","O","O","O","O","O","X","O","O","X","X","X","X","X","O"],["O","X","O","O","O","X","O","X","O","X","X","O","X","X","X","X","X","X","O","O"],["X","X","O","X","O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","X"],["O","X","O","O","X","X","X","O","O","O","X","X","X","X","X","X","X","O","O","O"],["O","O","X","X","X","O","O","O","X","X","X","X","X","X","X","X","O","O","O","O"],["X","O","O","X","O","X","O","O","O","O","X","X","X","X","X","X","X","O","X","X"],["X","O","X","O","O","O","O","O","O","X","X","X","X","X","X","X","O","O","O","O"],["O","X","X","O","O","O","X","X","X","X","X","X","X","O","X","X","X","X","O","O"],["O","X","O","O","O","O","X","X","X","X","X","X","X","O","O","X","O","O","X","X"],["O","O","O","O","O","O","X","X","X","X","O","X","O","O","O","X","X","O","O","O"]]

    s = Solution()
    s.solve(b)
    for i in range(len(b)):
        for j in range(len(t)):
            if b[i][j] != t[i][j]:
                print(i, '   ', j)