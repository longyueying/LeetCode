class Solution(object):

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N+1):
            if self.solver(str(i)):
                count+=1
        return count
    def solver(self, digit):
        if '3' in digit or '4' in digit or '7' in digit:
            return False
        elif '2' in digit or '5' in digit or '6' in digit or '9' in digit:
            return True
        else:
            return False


if __name__=="__main__":
    solu = Solution()
    print(solu.rotatedDigits(857))