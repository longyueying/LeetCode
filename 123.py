class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        maxprofit = 0
        min = prices[0]
        profitToEnd = [0]*len(prices)
        for i in range(1, len(prices)):
            if prices[i] - min > maxprofit:
                maxprofit = prices[i] - min
            elif prices[i] < min:
                min = prices[i]
            profitToEnd[i] = maxprofit

        max = prices[len(prices)-1]
        maxprofit = 0
        profitToBegin = [0]*len(prices)

        for i in range(len(prices)-2, -1,-1):
            if max - prices[i] > maxprofit:
                maxprofit = max - prices[i]
            elif prices[i] > max:
                max = prices[i]
            profitToBegin[i] = maxprofit
        maxprofit = profitToBegin[0]

        for i in range(1, len(prices)):
            if profitToBegin[i] + profitToEnd[i-1]> maxprofit:
                maxprofit = profitToBegin[i] + profitToEnd[i-1]
        return maxprofit