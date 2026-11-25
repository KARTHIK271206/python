# LeetCode 268: Missing Number (XOR approach)
class Solution:
    def missingNumber(self, nums):
        answer = len(nums)
        for i, value in enumerate(nums):
            answer ^= i ^ value
        return answer
# Example: [9,6,4,2,3,5,7,0,1] -> 8
