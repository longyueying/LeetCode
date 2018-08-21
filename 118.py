class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            arr = [1] * (i + 1)
            for j in range(1, i):
                arr[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(arr)
        return res