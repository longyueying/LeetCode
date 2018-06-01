class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while a & b !=0:

            temp = (a^b)
            b = (a & b) << 1
            a= temp
        return a^b

if __name__=='__main__':
    solu = Solution()
    print(solu.getSum(4,2))
