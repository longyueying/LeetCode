class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        str = list(s)
        str.reverse()

        i = 0
        while i < len(str)-1:
            if dic[str[i]] <= dic[str[i+1]]:
                res += dic[str[i]]
                i+=1
            else:
                res = res + dic[str[i]] - dic[str[i+1]]
                i+=2
        if i == len(str)-1:
            res += dic[str[i]]
        return res
