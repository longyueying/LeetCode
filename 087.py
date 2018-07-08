class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n,m = len(s1),len(s2)
        if n!=m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1==s2:
            return True
        for i in range(1,n):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:n], s2[i:n]):
                return True
            if self.isScramble(s1[0:i], s2[n-i:n]) and self.isScramble(s1[i:n], s2[0:n-i]):
                return True
        return False

if __name__=="__main__":
    solu = Solution()
    print(solu.isScramble("abcdefghijklmnopq","efghijklmnopqcadb"))