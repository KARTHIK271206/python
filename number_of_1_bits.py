# LeetCode 191: Number of 1 Bits
class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
# Example: binary 1011 -> 3
