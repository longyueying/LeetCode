class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index = -1
        head = [-1] * len(S)
        end = [-1]*len(S)

        for i in range(len(S)):
            if S[i] == C:
                index = i
            if index != -1:
                head[i] = i-index
        index = -1
        for i in range(len(S)-1, -1,-1):
            if S[i] == C:
                index = i
            if index != -1:
                end[i] = index -i
        # print(head)
        # print(end)
        for i in range(len(head)):
            if head[i] == -1:
                head[i] = end[i]
            elif end[i]!=-1:
                head[i] = min(head[i], end[i])
        return head

if __name__=="__main__":
    solu = Solution()
    print(solu.shortestToChar("abaa","b"))
