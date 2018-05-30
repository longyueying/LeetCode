class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rowbegin = 0
        rowend = n-1
        colbegin = 0
        colend= n-1

        ret = [[0 for col in range(n)] for row in range(n)]
        num = 1
        while rowbegin<=rowend and colbegin<=colend:
            for i in range(colbegin, colend+1):
                ret[rowbegin][i] = num
                num+=1

            rowbegin+=1

            if rowbegin<=rowend:
                for i in range(rowbegin, rowend+1):
                    ret[i][colend] = num
                    num+=1
            else:
                break

            colend-=1
            if colbegin<=colend:
                for i in range(colend,colbegin-1, -1):
                    ret[rowend][i] = num
                    num+=1
            else:
                break

            rowend-=1
            if rowbegin<=rowend:
                for i in range(rowend, rowbegin-1, -1):
                    ret[i][colbegin] = num
                    num+=1
            else:
                break
            colbegin+=1

        return ret

if __name__=="__main__":
    solu = Solution()
    print(solu.generateMatrix(3))