class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        end = -1
        dic  = {}
        begin = -1
        for i in range(len(s)):
            if s[i] in t:
                begin = i
                dic[s[i]] = i
                break
        if begin==-1:
            return ''

        for i in range(begin+1, len(s)):
            if s[i] in t:
                dic.setdefault(s[i], 0)
                if len(dic) == len(t):
                    
