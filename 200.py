from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        m = len(grid)
        if m ==0:
            return 0
        n = len(grid[0])
        quene = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res+=1
                    quene.append((i,j))
                    while quene:
                        k, q = quene.popleft()
                        if k>=0 and k < m and q >= 0 and q < n and grid[k][q]=='1':
                            grid[k][q]='0'
                            quene.extend([(k,q-1), (k,q+1),(k+1, q), (k-1,q)])
        return res

if __name__=='__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
