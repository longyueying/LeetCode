class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        stairs_list = [0]*n
        stairs_list[0] = 1
        stairs_list[1] = 2

        for i in range(2,n):
            stairs_list[i] = stairs_list[i-1]+stairs_list[i-2]
        return stairs_list[n-1]

if __name__=='__main__':
    solu = Solution()
    print(solu.climbStairs(2))
