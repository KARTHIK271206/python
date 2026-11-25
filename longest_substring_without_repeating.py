# LeetCode 3: Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen, left, best = {}, 0, 0
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            best = max(best, right - left + 1)
        return best
# Example: "abcabcbb" -> 3
