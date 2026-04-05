class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        theMin = prices[0]
        theMax = prices[0]
        i = 0

        while i < len(prices):
            if prices[i] < theMin:
                theMin = prices[i]
                theMax = prices[i]
            if prices[i] > theMax:
                theMax = prices[i]
                x = theMax - theMin
                res = max(x, res)
            i = i + 1
        return res

        