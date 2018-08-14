class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j=0
        while i < m and j<n:
                if nums1[i] <= nums2[j]:
                    i+=1
                else:
                    begin = j
                    while j < n and nums1[i] > nums2[j]:
                        j+=1
                    end = j

                    num = end - begin
                    nums1[i+num:m+num] = nums1[i:m]
                    nums1[i:i+num] = nums2[begin:end]
                    m = m+num
                    i+=num
        if m < len(nums1):
            nums1[m:len(nums1)] = nums2[j:]
        return nums1
if __name__=="__main__":
    s = Solution()
    print(s.merge([2,0],1,[1],1))