# LeetCode 238: Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        prefix = 1
        for i, value in enumerate(nums):
            result[i] = prefix
            prefix *= value
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

# Example: [1,2,3,4] -> [24,12,8,6]
