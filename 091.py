class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 1
        length = len(s)
        dp = [0]*length

        if length==1:
            if int(s)==0:
                return 0
            else:
                return 1
        dp[0] = 1
        if int(s[1])==0 or int(s[:2])>26:
            dp[1] = 1
        else:
            dp[1] = 2

        for i in range(2, length):
            if int(s[i])!=0:
                dp[i]+=dp[i-1]
            if int(s[i-1:i+1]) <=26:
                dp[i]+=dp[i-2]
        return dp[-1]