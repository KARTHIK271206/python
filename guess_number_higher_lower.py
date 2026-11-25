# LeetCode 374: Guess Number Higher or Lower
# The LeetCode judge provides guess(num).
class Solution:
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0:
                right = mid - 1
            else:
                left = mid + 1
