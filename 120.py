class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length == 0:
            return 0
        elif length==1:
            return triangle[0][0]
        else:
            dp = [0]*length
            dp[0] = triangle[0][0]
            print(dp)
            for i in range(1,length):
                dp[i] = triangle[i][i] + dp[i - 1]
                for j in range(i-1, 0,-1):
                    dp[j] = min(triangle[i][j]+dp[j-1], triangle[i][j]+dp[j])
                dp[0] = triangle[i][0] + dp[0]
            return min(dp)
if __name__=="__main__":
    s = Solution()
    t = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(s.minimumTotal(t))