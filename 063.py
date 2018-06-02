class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path_list = [[1 for j in range(n)] for i in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                for p in range(j, n):
                    path_list[0][p] = 0
                break

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for p in range(i, m):
                    path_list[p][0] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    path_list[i][j] = 0
                else:
                    path_list[i][j] = path_list[i-1][j] + path_list[i][j-1]
        return path_list[m-1][n-1]
if __name__ == "__main__":
    solu = Solution()
    print(solu.uniquePathsWithObstacles([[0],[1]]))