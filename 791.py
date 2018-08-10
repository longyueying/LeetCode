class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic_order = {}
        dic_word = {}
        for i in range(len(S)):
            dic_word.setdefault(S[i],0)
            dic_order[i] = S[i]

        for i in range(len(T)):
            dic_word.setdefault(T[i], 0)
            dic_word[T[i]]+=1
        s = ''
        for i in range(len(S)):
            s+=(dic_order[i]*dic_word[dic_order[i]])
            dic_word[dic_order[i]] = 0
        for k in dic_word:
            s+= (k*dic_word[k])
        return s
if __name__=="__main__":
    solu = Solution()
    print(solu.customSortString('cba', 'abcd'))