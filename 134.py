class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gap = [0]*len(gas)
        for i in range(len(gas)):
            gap[i] = gas[i] - cost[i]

        max_gap = min(gap)

        if sum(gap) < 0:
            return -1
        else:
            begin = 0
            total = 0
            i = 0
            while i < len(gas):
                total += gap[i]
                i+=1
                if total < 0:
                    begin = i
                    total = 0
        return begin
if __name__=="__main__":
    s = Solution()
    print(s.canCompleteCircuit([3,3,4],[3,4,4]))