# LeetCode 67: Add Binary
class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
# Example: a="11", b="1" -> "100"
