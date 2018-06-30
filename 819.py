class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = paragraph.split(' ')
        res = {}
        for word in paragraph:
            if len(word)> 0 and (ord(word[-1]) < ord('a') or ord(word[-1]) > ord('z')):
                word = word[:-1]
            res.setdefault(word, 0)
            res[word]+=1
        max = 0
        key = ''
        for k in res.keys():
            if k not in banned:
                if res[k] > max:
                    max = res[k]
                    key = k
        return key
if __name__=='__main__':
    solu = Solution()
    print(solu.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))