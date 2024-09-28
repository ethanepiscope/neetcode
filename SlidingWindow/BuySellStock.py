# Easy peasy O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > profit:
                profit = p - minPrice
        return profit