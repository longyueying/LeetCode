class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroRow = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRow = i
                    break
        if zeroRow==-1:
            return matrix
        for i in range(n):
            if matrix[zeroRow][i] == 0:
                matrix[zeroRow][i] = 1
            else:
                matrix[zeroRow][i] = 0
        row = False
        for i in range(0,zeroRow):
            row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    row = True
                    matrix[zeroRow][j] = 1
            if row == True:
                for j in range(n):
                    matrix[i][j]=0
        for i in range(zeroRow+1, m):
            row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    row = True
                    matrix[zeroRow][j] = 1
            if row == True:
                for j in range(n):
                    matrix[i][j] = 0
        for j, flag in enumerate(matrix[zeroRow]):
            if flag ==1:
                for i in range(m):
                    matrix[i][j]=0

        return matrix
if __name__=="__main__":
    solu = Solution()
    print(solu.setZeroes([[1]]))