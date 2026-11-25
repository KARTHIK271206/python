# LeetCode 27: Remove Element
class Solution:
    def removeElement(self, nums, val):
        write = 0
        for value in nums:
            if value != val:
                nums[write] = value
                write += 1
        return write

# Example: [3,2,2,3], val=3 -> length 2
