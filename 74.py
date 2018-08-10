class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        if r == 0:
            return False

        c = len(matrix[0])
        if c==0:
            return False
        if target < matrix[0][0]:
            return False


        begin = 0
        end = r
        while end - begin > 1:
            mid  = int((end+begin)/2)
            if matrix[mid][0] <= target:
                begin = mid
            else:
                end = mid

        row = begin
        print(row)
        begin=0
        end = c-1
        while begin<=end:
            mid = int((end+begin)/2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                begin = mid+1
            else:
                end = mid -1
        return False
if __name__=="__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))

