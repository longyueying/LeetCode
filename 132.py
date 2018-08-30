class Solution(object):
    def isPa(self,s):
        i = 0
        j = len(s)-1
        while j > i:
            if s[i]!=s[j]:
                return False
            j-=1
            i+=1
        return True
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 0
        N = len(s)
        dp = list(range(-1, N))
        for i in range(N):
            for j in range(i,N):
                if self.isPa(s[i:j+1]):
                    dp[j+1] = min(dp[i]+1, dp[j+1])
        return dp[-1]

if __name__=="__main__":
    s = Solution()
    print(s.minCut('aab'))
