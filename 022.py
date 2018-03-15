class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combination = []
        self.generate(n, n, '', combination)
        return combination

    def generate(self, left, right, temp, comb):
        if left > right or left < 0 or right < 0:
            return
        elif left == 0 and right ==0:
            comb.append(temp)
        else:
                self.generate(left-1, right, temp+'(', comb)
                self.generate(left, right-1, temp+')', comb)

if __name__=="__main__":
    solu = Solution()
    print(solu.generateParenthesis(2))



