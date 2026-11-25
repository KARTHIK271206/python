# LeetCode 349: Intersection of Two Arrays
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

# Example: [1,2,2,1], [2,2] -> [2]
