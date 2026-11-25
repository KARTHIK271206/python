# LeetCode 70: Climbing Stairs
class Solution:
    def climbStairs(self, n):
        one, two = 1, 1
        for _ in range(n - 1):
            one, two = one + two, one
        return one
# Example: n=5 -> 8
