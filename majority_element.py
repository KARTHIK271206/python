# LeetCode 169: Majority Element
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            count += 1 if value == candidate else -1
        return candidate

# Example: [3,2,3] -> 3
