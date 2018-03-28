wordDict = {}
words = ['a', 'b', 'c', 'b']

for word in words:
    wordDict.setdefault(word, 0)
    wordDict[word]+=1

print(wordDict)

print(words.count('d'))
