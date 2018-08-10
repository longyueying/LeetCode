class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if len(S)==0:
            return [0,0]
        a = 1
        b = 0
        total = 100
        for i in range(len(S)):
            s = S[i]
            if b+widths[ord(s) - ord('a')] > 100:
                a+=1
                b = widths[ord(s) - ord('a')]
            else:
                b+= widths[ord(s) - ord('a')]
        return [a, b]

if __name__=="__main__":
    solu = Solution()
    print(solu.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))