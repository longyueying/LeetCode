class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 :
            return [-1,-1]

        start = 0
        end = len(nums)-1

        while start <= end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                leftend = mid
                rightstart = mid
                break
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        if start > end:
            return [-1,-1]

        leftstart = 0
        rightend = len(nums) - 1
        while leftstart < leftend:
            mid = int((leftstart+leftend)/2)
            if nums[mid] == target:
                leftend = mid
            else:
                leftstart = mid+1

        while rightstart < rightend:
            mid = int((rightstart+rightend+1)/2)
            if nums[mid] == target:
                rightstart = mid
            else:
                rightend = mid-1
        return [leftstart, rightend]

if __name__ == "__main__":
    solution = Solution()
    nums = [5,7,7,8,8,10]
    print(solution.searchRange(nums, 8))
