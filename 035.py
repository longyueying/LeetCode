class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if end < 0:
            return 0

        while start <= end:
            if start == end:
                if nums[start]==target:
                    return start
                elif nums[start] > target:
                    return start
                else:
                    return start+1

            mid = int((start+end)/2)
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid

if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5,6]
    print(solution.searchInsert(nums, 2))