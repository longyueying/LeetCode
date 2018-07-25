class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        length = len(machines)
        if sum(machines)%length!=0:
            return -1
        s = 0
        avg = sum(machines)/length
        res = 0
        for i in range(len(machines)):
            if machines[i]<avg:
                res+=(avg-machines)
        return res