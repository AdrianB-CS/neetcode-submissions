class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggestProfit = 0
        minPurchasePrice = prices[0]
        
        for price in prices:

            if price < minPurchasePrice:
                minPurchasePrice = price
            deltaPrice = price - minPurchasePrice

            if deltaPrice > biggestProfit:
                biggestProfit = deltaPrice
                
        return biggestProfit




            

                


