class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]*(n+1)

        for i in range(1, n+1):
            sum = 0
            for j in range(i):
                sum+=dp[j]*dp[i-j-1]
            dp[i] = sum
        print(dp)
        return dp[-1]

if __name__=="__main__":
    s = Solution()
    print(s.numTrees(3))