class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        stack = [(0, [], -1)]

        candidates.sort()

        while len(stack) > 0:
            sum, temp, pos = stack.pop()
            i = len(candidates) - 1
            while i > pos:
                if sum + candidates[i] < target:
                    if i - candidates.count(candidates[i]) <= pos:
                        stack.append((sum+candidates[i], temp+[candidates[i]], pos + 1))
                    else:
                        stack.append((sum + candidates[i], temp + [candidates[i]], i-candidates.count(candidates[i])+1))
                elif sum + candidates[i] == target:
                    res.append(temp+[candidates[i]])

                i = i - candidates.count(candidates[i])
        return res

if __name__ == "__main__":
    solu = Solution()
    print(solu.combinationSum2([2,5,2,1,2], 5))




