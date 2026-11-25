# LeetCode 242: Valid Anagram
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

# Example: Solution().isAnagram("anagram", "nagaram") -> True
