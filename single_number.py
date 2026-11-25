# LeetCode 136: Single Number
class Solution:
    def singleNumber(self, nums):
        answer = 0
        for value in nums:
            answer ^= value
        return answer

# Example: [4,1,2,1,2] -> 4
