class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(s)
        stackTop = -1
        subLen = 0
        maxLen = 0

        for i in range(strLen):
            if s[i] == '(':
                stackTop+=1
            else:
                if stackTop < 0:
                    subLen = 0
                else:
                    stackTop-=1
                    subLen+=2
                    if stackTop < 0:
                        if subLen > maxLen:
                            maxLen = subLen

        stackTop = -1
        subLen = 0
        for i in range(strLen-1, -1, -1):
            if s[i] == ')':
                stackTop+=1
            else:
                if stackTop < 0:
                    subLen = 0
                else:
                    stackTop-=1
                    subLen+=2
                    if stackTop < 0:
                        if subLen > maxLen:
                            maxLen = subLen

        return maxLen

if __name__=="__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")()(((())))("))



