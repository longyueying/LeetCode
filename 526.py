class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.res = 0
        index_arr = [i for i in range(1, N+1)]

        def solver(n, index_arr):
            if len(index_arr) == 0:
                self.res+=1
            else:
                for index in index_arr:
                    if n % index==0 or index%n==0:
                        tmp = index_arr[:]
                        tmp.remove(index)
                        solver(n+1, tmp)
        solver(1, index_arr)
        return self.res

