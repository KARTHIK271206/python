# LeetCode 69: Sqrt(x)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right

# Example: 8 -> 2
