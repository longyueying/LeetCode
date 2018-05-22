class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range((int(len(matrix)/2))):
            for j in range(i, len(matrix)-i-1):
                temp1 = matrix[i][j]
                temp2 = matrix[j][len(matrix)-i-1]
                temp3 = matrix[len(matrix)-i-1][len(matrix)-j-1]
                temp4 = matrix[len(matrix)-j-1][i]
                matrix[i][j] = temp4
                matrix[j][len(matrix) - i - 1] = temp1
                matrix[len(matrix) - i - 1][len(matrix) - j - 1] = temp2
                matrix[len(matrix) - j - 1][i] = temp3
            print(matrix)



if __name__=="__main__":
    solu = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    solu.rotate(mat)
    print(mat)