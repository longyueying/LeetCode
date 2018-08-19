class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m = len(matrix)
        n = len(matrix[0])

        left = [0]*n
        right = [n-1]*n
        hight = [0]*n
        maxArea = 0
        for i in range(m):
            cur_left=0
            cur_right = n-1
            for j in range(n):
                if matrix[i][j] == '0':
                    hight[j] = 0
                    cur_left = j+1
                    left[j] = 0
                else:
                    left[j] = max(cur_left, left[j])
                    hight[j]+=1

            for j in range(n-1, -1, -1):
                if matrix[i][j] == '0':
                    cur_right = j-1
                    right[j] = n-1
                else:
                    right[j] = min(cur_right, right[j])

            for j in range(n):
                maxArea = max(maxArea, hight[j]*(right[j]-left[j]+1))
        return maxArea

if __name__=="__main__":
    matrix = [["0","1","1","0","1"],
              ["1","1","0","1","0"],
              ["0","1","1","1","0"],
              ["1","1","1","1","0"],
              ["1","1","1","1","1"],
              ["0","0","0","0","0"]]
    s = Solution()
    print(s.maximalRectangle(matrix))





