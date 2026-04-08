class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDifference = 0
        maxAmount, minAmountIdx, minAmount = 0,0,0
        for i in range(0,len(prices)):

            if(i == 0):
                print("GOT HERE 0")
                minAmount = prices[i]
                maxAmount = prices[i]
                print("MIN AMOUNT: " + str(minAmount))
                print("MAX AMOUNT: " + str(maxAmount))
            
            if(minAmount > prices[i]):
                print("GOT HERE 1")
                minAmount = prices[i]
                minAmountIdx = i
                maxAmount = 0
                print("MIN AMOUNT: " + str(minAmount))
                print("MIN AMOUNT IDX: " + str(minAmountIdx))

            if(i > minAmountIdx and maxAmount < prices[i]):
                print("GOT HERE 2")
                maxAmount = prices[i]
                print("MAX AMOUNT: " + str(maxAmount))

            maxDifference = max(maxDifference, maxAmount - minAmount)
            print("MAX DIFFERENCE: " + str(maxDifference))

        return maxDifference
            

            


            
        