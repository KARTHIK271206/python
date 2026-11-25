# LeetCode 198: House Robber
class Solution:
    def rob(self, nums):
        two_back = one_back = 0
        for money in nums:
            two_back, one_back = one_back, max(one_back, two_back + money)
        return one_back
# Example: [2,7,9,3,1] -> 12
