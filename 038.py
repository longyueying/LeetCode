class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return '1'
        temp = self.countAndSay(n-1)
        result = ''

        begin = 0
        count = 1
        for i in range(1, len(temp)):
            if int(temp[i]) == int(temp[begin]):
                count += 1
            else:

                result = result+str(count)
                result = result+temp[begin]
                count = 1
                begin = i
        result = result+str(count)
        result = result+temp[begin]

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(4))
