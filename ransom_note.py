# LeetCode 383: Ransom Note
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        available = Counter(magazine)
        for char in ransomNote:
            if available[char] == 0: return False
            available[char] -= 1
        return True
# Example: "aa", "aab" -> True
