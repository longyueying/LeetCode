class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s_reverse = S[::-1]
        s_list = set(list(S))
        dic = {}
        for c in s_list:
            dic[c] = -1
        for i in range(len(s_reverse)):
            if dic[s_reverse[i]] == -1:
                dic[s_reverse[i]] = len(S)-i-1

        begin = -1
        end = -1
        res = []
        for i in range(len(S)):
            if dic[S[i]] > end:
                end = dic[S[i]]
            if i == end:
               res.append(end - begin)
               begin = i
        return res
if __name__=="__main__":
    solu = Solution()
    print(solu.partitionLabels("ababcbacadefegdehijhklij"))

