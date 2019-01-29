
class Solution:
    def calculate_factorial(self, n):
        result = 1
        for i in range(1, n+1, 1):
            result = result * i
        return result 

    def trailingZeroes_complex(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        factorial = self.calculate_factorial(n)
        factorial = str(factorial)
        for i in range(len(factorial)-1, -1, -1):
            if factorial[i] == '0':
                res += 1
            else:
                break
        return res
   
    def trailingZeroes(self, n):
        res = 0
        divisor = 5
        while divisor <= n:
            res = res + int(n / divisor)
            divisor = divisor * 5
        return res

if __name__ == "__main__":
    n = 6
    solution = Solution()
    print(solution.trailingZeroes(n))
