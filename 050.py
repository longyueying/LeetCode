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
            result = x
            for i in range(n-2):
                result = result * x
            return result

if __name__ == "__main__":
    solution = Solution()
    solution.myPow(2.0, 10)