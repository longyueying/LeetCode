class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list = list(s)
        t_list = list(t)
        for c in s_list:
            t_list.remove(c)
        return ''.join(t_list)

if __name__=="__main__":
    solu = Solution()
    print(solu.findTheDifference('abcd', 'abcde'))