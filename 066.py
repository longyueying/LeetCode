class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        carry = 1

        for i in range(len(digits)):
            digits[i] += carry
            carry = int(digits[i]/10)
            digits[i] = digits[i]%10
        if carry==1:
            digits.append(1)

        digits.reverse()
        return digits

if __name__=="__main__":
    solu = Solution()
    print(solu.plusOne([9,9,9,9]))
