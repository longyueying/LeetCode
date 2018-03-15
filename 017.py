class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapList = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]

        inlength = len(digits)
        if(inlength == 0):
            return []
        outLength = 1
        for digitchar in range(inlength):
            digit = int(digits[digitchar])
            index = digit - 2
            outLength = outLength * len(mapList[index])

        repeatTime = outLength
        cycleTime = 1
        outList = []

        for i in range(outLength):
            outList.append([])

        for digitchar in range(inlength):
            digit = int(digits[digitchar])
            index = digit - 2
            repeatTime = int(repeatTime / len(mapList[index]))

            for i in range(cycleTime):
                for j in range(len(mapList[index])):
                    for k in range(repeatTime):
                        outList[i*repeatTime*len(mapList[index]) + j*repeatTime + k].append(mapList[index][j])

            cycleTime = cycleTime * len(mapList[index])
        returnList = []
        for str in outList:
            returnList.append(''.join(letter for letter in str))
        return returnList

if  __name__== "__main__":
    solution = Solution()
    print(solution.letterCombinations('23'))




