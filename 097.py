class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)

        if len_s1 + len_s2 != len_s3:
            return False

        dp = [[0] * (len_s2 + 1) for i in range(len_s1 + 1)]

        dp[0][0] = 1

        for i in range(1, len_s1 + 1):
            if (s1[i - 1] == s3[i - 1] and dp[i-1][0] == 1):
                dp[i][0] = 1

        for j in range(1, len_s2 + 1):
            if (s2[j - 1] == s3[j - 1] and dp[0][j - 1] == 1):
                dp[0][j] = 1

        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if (dp[i][j - 1] == 1 and s2[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] == 1 and s1[i - 1] == s3[i + j - 1]):
                    dp[i][j] = 1
        print(dp)
        if dp[len_s1][len_s2] == 1:
            return True
        else:
            return False

if __name__=="__main__":
    s = Solution()
    print(s.isInterleave("aabcc","dbbca","aadbbcbcac"))