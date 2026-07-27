# given array of prices (integer) find the max profit and return it by determining
# best time to buy and sell stocks
# approach: two pointer (under sliding window in neetcode)
# time complexity: O(n)
# left is buy time, right is sell time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit

