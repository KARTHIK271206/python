# LeetCode 746: Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost):
        one_back = two_back = 0
        for value in cost:
            one_back, two_back = value + min(one_back, two_back), one_back
        return min(one_back, two_back)
# Example: [10,15,20] -> 15
