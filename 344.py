class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s

        s = list(s)
        # begin = 0
        # end = length-1
        # while begin< end:
        #     temp = s[begin]
        #     s[begin]= s[end]
        #     s[end] = temp
        #     begin+=1
        #     end-=1
        # return ''.join(s)
        s.reverse()
        return ''.join(s)

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverseString('hello'))