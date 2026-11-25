# LeetCode 152: Maximum Product Subarray
class Solution:
    def maxProduct(self, nums):
        high = low = answer = nums[0]
        for value in nums[1:]:
            if value < 0: high, low = low, high
            high = max(value, high * value)
            low = min(value, low * value)
            answer = max(answer, high)
        return answer
# Example: [2,3,-2,4] -> 6
