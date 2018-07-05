class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column_max = []
        row_max = []

        side_len = len(grid)
        for i in range(side_len):
            c_max = 0
            r_max = 0
            for j in range(side_len):
                if grid[i][j] > r_max:
                    r_max = grid[i][j]
                if grid[j][i] > c_max:
                    c_max = grid[j][i]
            column_max.append(c_max)
            row_max.append(r_max)
        sum = 0
        for i in range(side_len):
            for j in range(side_len):
                temp = min(row_max[i],column_max[j])
                if temp > grid[i][j]:
                    sum = sum+(temp - grid[i][j])
        return sum