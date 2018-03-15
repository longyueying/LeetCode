class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        length = len(s)

        for i in range(length):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(s[i])

            if s[i] == '}' or s[i] == ']' or s[i] == ')':
                if len(stack) == 0:
                    return False
                topChar = stack.pop()
                if s[i] == '}':
                    if topChar != '{':
                        return False
                if s[i] == ']':
                    if topChar != '[':
                        return False
                if s[i] == ')':
                    if topChar != '(':
                        return False

        if len(stack) == 0:
            return True
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.isValid('()'))