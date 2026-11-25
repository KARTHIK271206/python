# LeetCode 58: Length of Last Word
class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1]) if words else 0
# Example: "Hello World" -> 5
