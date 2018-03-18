class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        if divisor == 0 or (dividend == INT_MIN and divisor == -1):
            return INT_MAX

        if (dividend > 0) == (divisor >0):
            sign = 1
        else:
            sign = -1

        re = 0
        m = abs(dividend)
        n = abs(divisor)

        while (m >= n):

            t = n
            p = 1
            while(m >= (t<<1)):
                t = t<<1
                p = p<<1
            re+=p
            m-=t
        if sign==1:
            return re
        else:
            return -re



if __name__=="__main__":
    solu = Solution()
    print(solu.divide(-1, -1))