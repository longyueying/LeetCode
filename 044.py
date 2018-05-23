class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(2)]
        dp[0][0] = True
        for i in range(1, 2):
            dp[i][0] = False
        for j in range(1, n+1):
            dp[0][j] = True if p[j-1] == '*' else False
            dp[0][j] = dp[0][j] and dp[0][j-1]
        for i in range(1, m+1):
            dp[i%2][0] = False
            for j in range(1, n+1):
                if p[j-1] != '*':
                    dp[i%2][j] = dp[(i-1)%2][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[i%2][j] = dp[(i-1)%2][j] or dp[i%2][j-1]
        return dp[m%2][n]

if __name__ == "__main__":
    solu = Solution()
    print(solu.isMatch("aa"
,"*"))
