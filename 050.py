class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n==0:
            return 1
        elif n==1:
            return x
        else:
            if n < 0:
                x = 1/x
                n = -n
            result = x

            if n % 2 == 0:
                result = self.myPow(x*x, n/2)
            else:
                n = n-1
                result = x*self.myPow(x*x, n/2)
            return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(0.00001,2147483647))