class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while (i+1)*9*(pow(10, i)) < n:
            n -= ((i+1)*9*(pow(10, i)))
            i += 1
        first = pow(10, i)
        num = first + int(n/(i+1))
        index = n % (i+1)


        if index == 0:
            return (num-1) % 10
        else:
            #num+=1
            l = []
            while num!=0:
                temp = num % 10
                l.insert(0, temp)
                num = int(num/10)
            return l[index-1]
if __name__=='__main__':
    solu = Solution()
    print(solu.findNthDigit(11))

