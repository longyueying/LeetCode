import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        length = len(tokens)
        for i in range(length):
            print(stack)
            if tokens[i] == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif tokens[i] == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif tokens[i] == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif tokens[i] == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operator.truediv(a, b)))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]

if __name__=="__main__":
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))