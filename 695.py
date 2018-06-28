class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               ans = max(ans, self.solver(grid, i, j))
        return ans
    def solver(self, grid, i, j):
        if i < len(grid) and j < len(grid[0]) and i >=0 and j>=0 and grid[i][j]==1:
            grid[i][j]=0
            return (1+self.solver(grid,i-1,j)+self.solver(grid,i,j-1)+self.solver(grid,i+1,j)+self.solver(grid,i,j+1))
        return 0
if __name__=="__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    solu = Solution()
    print(solu.maxAreaOfIsland(grid))