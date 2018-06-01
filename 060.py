class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = [(i+1) for i in range(n)]
        ret = ''
        k = k-1
        nums = 1
        for i in range(1, n):
            nums = nums*i

        for i in range(n-1, 0, -1):
            idx = int(k / nums)
            ret = ret+chr(ord('0')+l[idx])
            l.remove(l[idx])
            k = k % nums
            nums = int(nums/i)
        ret = ret+chr(ord('0')+l[0])
        return ret

if __name__=='__main__':
    solu = Solution()
    print(solu.getPermutation(4,9))