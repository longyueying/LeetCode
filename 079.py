class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        self.res = False
        m = len(board)
        n = len(board[0])
        invisited = [[0]*n for i in range(m)]

        def solver(h, v, status):
            if len(status) == 0:
                self.res = True
                return
            else:
                if h-1 >=0 and invisited[h - 1][v]==0:
                    if board[h - 1][v] == status[0]:
                        invisited[h - 1][v] = 1
                        status.pop(0)
                        solver(h - 1, v, status)
                        status.insert(0, board[h - 1][v])
                        invisited[h - 1][v] = 0
                if v-1>=0 and invisited[h][v-1]==0:
                    if board[h][v-1] == status[0]:
                        invisited[h][v - 1] = 1
                        status.pop(0)
                        solver(h, v-1, status)
                        status.insert(0, board[h][v-1])
                        invisited[h][v - 1] = 0
                if h+1 <m and invisited[h + 1][v]==0:
                    if board[h + 1][v] == status[0]:
                        invisited[h + 1][v] = 1
                        status.pop(0)
                        solver(h + 1, v, status)
                        status.insert(0, board[h + 1][v])
                        invisited[h + 1][v] = 0
                if v+1 < n and invisited[h][v+1]==0:
                    if board[h][v+1] == status[0]:
                        invisited[h][v + 1] = 1
                        status.pop(0)
                        solver(h, v+1, status)
                        status.insert(0, board[h][v+1])
                        invisited[h][v + 1] =0

        word = list(word)
        for i in range(m):
            for j in range(n):
                if self.res==True:
                    return self.res
                if board[i][j] == word[0]:
                    invisited[i][j] = 1
                    w = word.pop(0)
                    solver(i, j, word)
                    word.insert(0,w)
                    invisited[i][j] = 0
        return self.res

if __name__=="__main__":
    board = [["a","a"]]
    word = 'aaa'
    s = Solution()
    print(s.exist(board,word))