# LeetCode 1480: Running Sum of 1d Array
class Solution:
    def runningSum(self, nums):
        total = 0
        result = []
        for value in nums:
            total += value
            result.append(total)
        return result

# Example: [1,2,3,4] -> [1,3,6,10]
