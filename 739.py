class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        res = [0]*length

        stack = []

        for i in range(length):
            if len(stack)==0:
                stack.append(i)
            elif temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    res[index] = i - index
                stack.append(i)
        return res