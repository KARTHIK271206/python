# LeetCode 283: Move Zeroes
class Solution:
    def moveZeroes(self, nums):
        write = 0
        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0

# Example: [0,1,0,3,12] becomes [1,3,12,0,0]
