class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length==0:
            return 0
        dp = [[1]*length for i in  range(length)]
        for i in range(2,length+1):
            for j in range(length-i+1):
                if s[i+j-2] == s[i+j-1]:
                    min_val = dp[j][i+j-2]
                else:
                    min_val = dp[j][i + j - 2]+1
                for k in range(j, i+j-2):
                    if s[i+j-1] == s[k]:
                        tmp = dp[j][k]+ dp[k+1][i+j-2]
                    else:
                        tmp = dp[j][k]+ dp[k+1][i+j-2]+1

                    if tmp < min_val:
                        min_val = tmp
                dp[j][i+j-1] = min_val
        print(dp)
        return dp[0][length-1]

if __name__ =="__main__":
    solu = Solution()
    print(solu.strangePrinter('a'))



