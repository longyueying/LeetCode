class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[0]*length for i in range(length)]
        res = length

        for i in range(length):
            dp[i][i] = 1
        for i in range(length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res+=1
        for gap in range(3, length+1):
            for i in range(length - gap+1):
                if s[i] == s[i+gap-1] and dp[i+1][i+gap-2] == 1:
                    dp[i][i+gap-1] = 1
                    res+=1
        return res

if __name__=="__main__":
    solu = Solution()
    print(solu.countSubstrings("aba"))