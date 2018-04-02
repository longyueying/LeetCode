import time
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        这样就可以accepted
        if target in nums:
            return nums.index(target)
        else:
            return -1
        
        '''
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        start = 0
        end = len(nums)-1

        pivot = self.seachPivot(nums, start, end)
        print(pivot)

        if target >= nums[start] and target <= nums[pivot]:
            return self.binarySearch(nums,start, pivot, target)
        elif target >= nums[pivot+1] and target <= nums[end]:
            return self.binarySearch(nums, pivot+1, end, target)
        else:
            return -1
    def binarySearch(self, nums, start, end, target):
        '''
        :param nums:  List[int]
        :param start: int
        :param end: int
        :param target: int
        :return: int
        '''
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        mid = int((start + end)/2)
        if target > nums[mid]:
            return self.binarySearch(nums, mid+1, end, target)
        else:
            return self.binarySearch(nums, start, mid, target)
    def seachPivot(self, nums, start, end):
        if end - start == 1:
            return start
        mid = int((start+end)/2)
        if nums[start] > nums[mid]:
            return self.seachPivot(nums, start, mid)
        else:
            return self.seachPivot(nums, mid, end)

    def searchSimple(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__=="__main__":
    nums = []
    for i in range(365, 500):
        nums.append(i)
    for i in range(1, 365):
        nums.append(i)
    solution = Solution()

    startTime = round(time.time()*1e10)
    print(solution.search(nums, 111))
    endTime = round(time.time()*1e10)
    print(endTime-startTime)

    startTime = round(time.time()*1e10)
    print(solution.searchSimple(nums, 111))
    endTime = round(time.time()*1e10)
    print(endTime-startTime)