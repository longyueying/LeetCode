class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x

        begin = 1
        end = x
        while begin < end:
            mid = int((begin+end)/2)
            if mid*mid < x:
                begin = mid+1
            elif mid*mid>x:
                end = mid
            else:
                return mid
        return begin-1

if __name__=="__main__":
    solu = Solution()
    print(solu.mySqrt(10))