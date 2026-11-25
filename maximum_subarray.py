# LeetCode 53: Maximum Subarray
class Solution:
    def maxSubArray(self, nums):
        current = best = nums[0]
        for value in nums[1:]:
            current = max(value, current + value)
            best = max(best, current)
        return best

# Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6
