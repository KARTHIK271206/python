#Write a function to find the longest common prefix string amongst an array of strings.
#include <string>
#include <vector>

class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if (strs.empty()) return "";
        
        // Loop through each character of the first string
        for (int i = 0; i < strs[0].length(); i++) {
            char currentChar = strs[0][i];
            
            // Compare this character with the same position in all other strings
            for (int j = 1; j < strs.size(); j++) {
                // If index exceeds string length or characters mismatch, stop
                if (i == strs[j].length() || strs[j][i] != currentChar) {
                    return strs[0].substr(0, i);
                }
            }
        }
        
        return strs[0];
    }
};
