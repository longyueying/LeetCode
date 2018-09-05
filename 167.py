class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        begin = 0
        end = length-1

        while begin < end:
            sum = numbers[begin]+numbers[end]
            if sum == target:
                break
            elif sum < target:
                begin+=1
            else:
                end-=1
        return [begin+1, end+1]