# LeetCode 387: First Unique Character in a String
class Solution:
    def firstUniqChar(self, s):
        counts = {}
        for char in s: counts[char] = counts.get(char, 0) + 1
        for i, char in enumerate(s):
            if counts[char] == 1: return i
        return -1
# Example: "leetcode" -> 0
