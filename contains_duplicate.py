# LeetCode 217: Contains Duplicate
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

# Example: Solution().containsDuplicate([1, 2, 3, 1]) -> True
