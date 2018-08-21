class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        tmp = t[0]
        length = len(s)
        if length<len(t):
            return 0
        pre = [0] * length
        for i in range(length):
            pre[i] = s[:i + 1].count(tmp)

        cur = [0] * length

        for i in range(1, len(t)):
            cur[i - 1] = 0
            tmp = t[i]
            for j in range(i, length):
                if tmp == s[j]:
                    cur[j] = cur[j - 1] + pre[j - 1]
                else:
                    cur[j] = cur[j - 1]
            pre = cur[:]
        return pre[-1]