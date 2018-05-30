class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[1:].islower():
            print(word[1:])
            return True
        return False

if __name__=='__main__':
    solu = Solution()
    print(solu.detectCapitalUse('Faslfdaf'))