class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDifference = 0
        maxAmount, minAmountIdx, minAmount = 0,0,0
        for i in range(0,len(prices)):

            if(i == 0):
                minAmount = prices[i]
                maxAmount = prices[i]
            
            if(minAmount > prices[i]):
                minAmount = prices[i]
                minAmountIdx = i
                maxAmount = 0

            if(i > minAmountIdx and maxAmount < prices[i]):
                maxAmount = prices[i]

            maxDifference = max(maxDifference, maxAmount - minAmount)

        return maxDifference
            

            


            
        