# LeetCode 5: Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):
        best = ""
        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > len(best): best = s[left:right + 1]
                    left -= 1
                    right += 1
        return best
# Example: "babad" -> "bab" or "aba"
