from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord in wordList:
            wordList.remove(beginWord)
        quene = deque([(beginWord, 1)])
        while quene:
            print(quene)
            word, length = quene.popleft()
            if word == endWord:
                return length
            for t in wordList[:]:
                if self.isTransform(word, t):
                    quene.append((t, length + 1))
                    wordList.remove(t)
        return 0

    def isTransform(self, current, target):
        if len(current) != len(target):
            return False
        i = 0
        j = len(current)-1
        while current[i] == target[i]:
            i += 1
        while current[j] == target[j]:
            j -= 1
        if i == j:
            return True
        else:
            return False

if __name__=="__main__":
    s = Solution()
    print(s.ladderLength('a', 'c', ["a","b","c"]))