class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # only track two things - lowest price and best profit
        maxP = 0
        minBuy = prices[0]
        
        for i in prices:
            maxP = max(maxP, i - minBuy) # passively tracking max profit 
            minBuy = min(minBuy, i) # is i the lowest price?
        
        return maxP


