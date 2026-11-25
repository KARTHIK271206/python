# LeetCode 121: Best Time to Buy and Sell Stock
# Given an array prices where prices[i] is the price of a stock on day i,
# find the maximum profit from one buy and one sell.
# If no profit is possible, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# Example:
# prices = [7, 1, 5, 3, 6, 4]
# print(Solution().maxProfit(prices))  # Output: 5
