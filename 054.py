class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        row_length = len(matrix)
        if row_length == 0:
            return []
        column_length = len(matrix[0])

        for i in range(int((row_length)/2)):
            if i < (column_length-i -1):
                for column in range(i, column_length-i):
                    ret.append(matrix[i][column])
                for row in range(i+1, row_length-i-1):
                    ret.append(matrix[row][column_length-i-1])
                for column in range(column_length-i-1, i-1, -1):
                    ret.append(matrix[row_length-i-1][column])
                for row in range(row_length-i-2, i, -1):
                    ret.append(matrix[row][i])
            elif column_length%2!=0:
                for j in range(i, row_length-i):
                    ret.append(matrix[j][int(column_length/2)])
                return ret
        if row_length%2!=0:
            row = int(row_length/2)
            if row < column_length-row:
                for column in range(row, column_length-row):
                    ret.append(matrix[row][column])
        return  ret



if __name__ == "__main__":
    solu = Solution()
    mat =[[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    print(solu.spiralOrder(mat))