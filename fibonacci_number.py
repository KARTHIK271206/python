# LeetCode 509: Fibonacci Number
class Solution:
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n): a, b = b, a + b
        return a
# Example: n=6 -> 8
