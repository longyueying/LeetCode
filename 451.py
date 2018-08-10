class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}

        for i in range(len(s)):
            dic.setdefault(s[i], 0)
            dic[s[i]]+=1

        tmp=[]
        for k in dic:
            i = 0
            while i < len(tmp) and dic[k] < dic[tmp[i]]:
                i+=1
            tmp.insert(i, k)
        res = []
        for k in tmp:
            res.extend([k]*dic[k])
        print(res)
        return ''.join(res)

if __name__=="__main__":
    solu = Solution()
    print(solu.frequencySort('tree'))