# LeetCode 125: Valid Palindrome
class Solution:
    def isPalindrome(self, s):
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]
# Example: "A man, a plan, a canal: Panama" -> True
