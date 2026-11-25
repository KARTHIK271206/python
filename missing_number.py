# LeetCode 268: Missing Number
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

# Example: [3,0,1] -> 2
