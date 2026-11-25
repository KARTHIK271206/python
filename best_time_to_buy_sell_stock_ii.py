# LeetCode 122: Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit

# Example: [7,1,5,3,6,4] -> 7
