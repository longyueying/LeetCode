class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 0:
            if n % 2 == 1:
                num+=1
            n = int(n /2)
        return num

if __name__=='__main__':
    solu = Solution()
    print(solu.hammingWeight(128))