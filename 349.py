class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dic = {}
        for i in nums1:
            nums1_dic.setdefault(i, 0)
            nums1_dic[i]+=1
        result = []
        nums2_set = set(nums2)
        for i in nums2_set:
            nums1_dic.setdefault(i, 0)
            if nums1_dic[i] > 0:
                result.append(i)
        return result

if __name__=="__main__":
    solu = Solution()
    print(solu.intersection([], [2,2]))