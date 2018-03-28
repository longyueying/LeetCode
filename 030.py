class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        rList = []

        strLen = len(s)
        wordsLen = len(words)
        wordLen = len(words[0])

        if strLen <= 0 or wordsLen <= 0:
            #print(strLen, wordsLen)
            return rList

        #print(strLen, wordsLen)
        wordsDict = {}
        tmpDict = {}
        for word in words:
            wordsDict.setdefault(word, 0)
            wordsDict[word]+=1

        #print(wordsDict)
        for i in range(wordLen):
            left = i
            tmpDict.clear()
            count = 0
            for j in range(i, strLen, wordLen):
                currentWord = s[j:j+wordLen]
                #print(currentWord)
                if words.count(currentWord):
                    tmpDict.setdefault(currentWord, 0)
                    tmpDict[currentWord] += 1
                    if tmpDict[currentWord] <= wordsDict[currentWord]:
                        count+=1
                    else:
                        while tmpDict[currentWord] > wordsDict[currentWord]:
                            leftword = s[left:left+wordLen]
                            if tmpDict[leftword] <= wordsDict[leftword]:
                                count-=1
                            tmpDict[leftword]-=1
                            left+=wordLen
                    if count == wordsLen:
                        rList.append(left)
                        tmpDict[s[left:left+wordLen]]-=1
                        left+=wordLen
                        count-=1

                else:
                    left = j + wordLen
                    tmpDict.clear()
                    count = 0
        return rList


if __name__ == "__main__":
    solution = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    #solution.findSubstring(s, words)
    print(solution.findSubstring(s, words))
