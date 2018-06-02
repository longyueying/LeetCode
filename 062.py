class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path_list = [[1 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                path_list[i][j] = path_list[i-1][j] + path_list[i][j-1]

        return path_list[m-1][n-1]


if __name__=='__main__':
    solu  = Solution()
    print(solu.uniquePaths(7,3))