class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [False]*(length+1)

        dp[0] = True
        for i in range(length+1):
            for word in wordDict:
                if len(word)>i:
                    continue
                elif s[i-len(word):i]==word and dp[i-len(word)]:
                    dp[i]=True
                    break
        return dp[-1]

if __name__=="__main__":
    s = "leetcode"
    w = ["leet", "code"]
    sr = Solution()
    print(sr.wordBreak(s, w))