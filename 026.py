def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return 0

    first = nums[0]
    length = 1

    for i in range(1, len(nums)):
        if nums[i] != first:
            first = nums[i]
            length+=1
            nums[length-1] = nums[i]
    return nums[0:length]


num = [1,1,2]
print(removeDuplicates(num))