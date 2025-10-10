# Name: Best Time to Buy and Sell Stock II
# Problem: Given array of stock prices, return the max profit that can be achieved
# if stocks can be sold multiple times throughout the week
# Approach: Find local min (valley) and local max (peak), subtract max from min

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = minPrice = maxPrice = profit = 0
        arrayLength = len(prices) - 1
        while i < arrayLength:
            # Stop when price is increasing, store it in minPrice (buy)
            while i < arrayLength and prices[i+1] <= prices[i]:
                i += 1
            minPrice = prices[i]
            # Stop when price is decreasing, best time to sell
            while i < arrayLength and prices[i+1] >= prices[i]:
                i += 1
            maxPrice = prices[i]
               
            profit += maxPrice - minPrice
        return profit

            

