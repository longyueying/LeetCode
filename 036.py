class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        usedRow = [[0 for i in range(9)] for j in range(9)]
        usedClomn = [[0 for i in range(9)] for j in range(9)]
        usedSuqare = [[0 for i in range(9)] for j in range(9)]

        result = True

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('0')
                    squareIndex = int(i/3) * 3 + int(j/3)
                    if usedRow[i][num-1] or usedClomn[j][num-1] or usedSuqare[squareIndex][num-1]:
                        result = False
                        return result
                    else:
                        usedRow[i][num - 1] = 1
                        usedClomn[j][num - 1] = 1
                        usedSuqare[squareIndex][num - 1] = 1

        return result

if __name__=="__main__":
    input = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    solution = Solution()
    if solution.isValidSudoku(input):
        print("True")
    else:
        print("False")
