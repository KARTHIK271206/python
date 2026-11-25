# LeetCode 11: Container With Most Water
class Solution:
    def maxArea(self, height):
        left, right, best = 0, len(height) - 1, 0
        while left < right:
            best = max(best, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return best
# Example: [1,8,6,2,5,4,8,3,7] -> 49
