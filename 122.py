class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices)-1):
            prices[i] = prices[i+1] - prices[i]
        for i in range(len(prices)-1):
            if prices[i]>0:
                sum+=prices[i]
        return sum