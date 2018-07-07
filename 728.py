class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for number in range(left, right+1):
            if self.isTarget(number):
                res.append(number)
        return res

    def isTarget(self, num):
        a = num
        while num > 0:
            temp = num % 10
            if temp==0:
                return False
            if a % temp != 0:
                return False
            num = int(num/10)
        return True
