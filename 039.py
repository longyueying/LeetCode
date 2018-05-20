class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        stack = [(0, [], 0)]

        while len(stack) > 0:
            sum, temp, pos = stack.pop()
            for i in range(len(candidates)-1, pos-1, -1):
                if target > sum+candidates[i]:
                    stack.append((sum+candidates[i], temp+[candidates[i]],i))
                elif target == sum+candidates[i]:
                    res.append(temp+[candidates[i]])

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.combinationSum([2,3,5], 8))
