class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x^y

        res = 0
        print('aaaa'.count('a'))
        while z > 0:
            if z % 2 ==1:
                res+=1
            z = int(z / 2)

        return res

if __name__=="__main__":
    solu = Solution()
    print(solu.hammingDistance(1,4))
