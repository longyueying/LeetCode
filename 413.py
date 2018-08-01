class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        length = len(A)
        res = 0
        if length < 3:
            return res

        def findBegin(head, A):
            while head <= len(A)-3:
                if A[head]-A[head+1] == A[head+1]-A[head+2]:
                    return head
                else:
                    head+=1
            return -1

        begin = findBegin(0, A)
        if begin==-1:
            return res
        else:
            res+=1
        i = begin+3

        while i < length:
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                res+=1
                i+=1
                if i >= length and begin < length-3:
                    begin = findBegin(begin + 1, A)
                    if begin == -1:
                        return res
                    else:
                        res += 1
                        i = begin + 3
            else:
                begin = findBegin(begin+1, A)
                if begin==-1:
                    return res
                else:
                    res+=1
                    i = begin+3

        return res

if __name__=="__main__":
    solu = Solution()
    print(solu.numberOfArithmeticSlices([1, 2, 3, 4]))
