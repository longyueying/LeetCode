class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums2sum = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                nums2sum.append(nums[i] + nums[j])
        #nums2sum = list(set(nums2sum))


        nums.sort()
        nums2sum.sort()

        begin = 0
        end = len(nums2sum)-1
        combination2 = []
        while(begin < end):
            sum = nums2sum[begin] + nums2sum[end]
            if sum == target:
                combination2.append([nums2sum[begin], nums2sum[end]])
                while begin+1 < len(nums2sum) and nums2sum[begin] == nums2sum[begin+1]:
                    begin+=1
                while end-1 > -1 and nums2sum[end] == nums2sum[end-1]:
                    end-=1
                begin += 1
                end -= 1
            elif sum > target:
                end-=1
            else:
                begin+=1
        #print(combination2)

        combination4 = []
        for mediumTarget in combination2:
            #print(mediumTarget)
            mediumTarget0 = mediumTarget[0]
            mediumTarget1 = mediumTarget[1]

            mediumCombination2Of0 = []
            mediumCombination2Of1 = []

            begin = 0
            end = len(nums)-1
            while (begin < end):
                sum = nums[begin] + nums[end]
                if sum == mediumTarget0:
                    mediumCombination2Of0.append([nums[begin], nums[end]])
                    #print([nums[begin], nums[end]])
                    while begin+1 < len(nums) and nums[begin] == nums[begin + 1]:
                        begin += 1
                    while end-1 > -1 and nums[end] == nums[end - 1]:
                        end -= 1
                    begin += 1
                    end -= 1
                elif sum > mediumTarget0:
                    end -= 1
                else:
                    begin += 1
            #print(mediumCombination2Of0)
            begin = 0
            end = len(nums)-1
            while (begin < end):
                sum = nums[begin] + nums[end]
                if sum == mediumTarget1:
                    mediumCombination2Of1.append([nums[begin], nums[end]])
                    #print([nums[begin], nums[end]])
                    while begin+1 < len(nums) and nums[begin] == nums[begin + 1]:
                        begin += 1
                    while end-1 > -1 and nums[end] == nums[end - 1]:
                        end -= 1
                    begin += 1
                    end -= 1
                elif sum > mediumTarget1:
                    end -= 1
                else:
                    begin += 1
            for mediumCombination0 in mediumCombination2Of0:
                for mediumCombination1 in mediumCombination2Of1:
                    unsort = mediumCombination0+mediumCombination1
                    unsort.sort()
                    combination4.append(unsort)

        removeindex = []

        for i in range(len(combination4)):
            for k in list(set(combination4[i])):
                if nums.count(k) < combination4[i].count(k):
                    removeindex.append(i)
                    #print(i)
                    break
            for j in range(i+1, len(combination4)):
                if combination4[i][0] == combination4[j][0] and combination4[i][2] == combination4[j][2] and combination4[i][1] == combination4[j][1] and combination4[i][3] == combination4[j][3]:
                    removeindex.append(j)
        removeindex = list(set(removeindex))
        returnIndex = list(range(len(combination4)))
        for index in removeindex:
            returnIndex.remove(index)

        #print(returnIndex)
        returnList = []
        for i in returnIndex:
            returnList.append(combination4[i])
        return returnList

if __name__=="__main__":
    arr = [0,0,0,0]
    solution = Solution()
    print(solution.fourSum(arr, 0))