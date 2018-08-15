class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <=1:
            return length
        count = 1
        cur = nums[0]
        begin =0
        end = 0

        i = 1
        while i < length:
            if nums[i] == cur:
                end = i
                count+=1
                i+=1
            else:
                cur = nums[i]
                if count <= 2:
                    count = 1
                    begin = i
                    end = i
                    i+=1
                else:
                    nums[begin+2:length+2-count] = nums[end+1:length]
                    length = length+2-count
                    begin = begin+2
                    end = begin+2
                    count = 1
                    i = begin+1
        if count > 2:
            length = length+2-count
        return length

if __name__ =="__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,2,3,3]))