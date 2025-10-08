// Name: Best time to buy and sell stocks
// Problem: Find the max profit that can be earned given an array of prices where i is the number of day
// Approach: Find the min value in the array, get the profit from current element minus min value
// Compare this profit with the max profit so far
class Solution {
    public int maxProfit(int[] prices) {
        // find minimum price
        int minIndex = 0;
        int minVal = prices[0];
        int profit = 0;
        int maxProfit = 0;
        for(int i=0;i<prices.length;i++){
            if(prices[i]<minVal){
                minVal = prices[i];
                minIndex = i;
            }
            // check profit for current price and min buying price
            profit = prices[i] - minVal;
            // compare this with the max profit so far
            maxProfit = Math.max(profit, maxProfit);
        }
        return maxProfit;
    }
}
