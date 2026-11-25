# LeetCode 461: Hamming Distance
class Solution:
    def hammingDistance(self, x, y):
        value, count = x ^ y, 0
        while value:
            count += value & 1
            value >>= 1
        return count
# Example: x=1, y=4 -> 2
