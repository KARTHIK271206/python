o#man numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#include <string>
#include <vector>

class Solution {
public:
    int romanToInt(std::string s) {
        int totalSum = 0;
        
        // Use an array mapping ASCII values directly for O(1) lookups
        std::vector<int> romanValues(128, 0);
        romanValues['I'] = 1;
        romanValues['V'] = 5;
        romanValues['X'] = 10;
        romanValues['L'] = 50;
        romanValues['C'] = 100;
        romanValues['D'] = 500;
        romanValues['M'] = 1000;
        
        for (int i = 0; i < s.length(); i++) {
            // Check if subtraction rule applies
            if (i + 1 < s.length() && romanValues[s[i]] < romanValues[s[i + 1]]) {
                totalSum -= romanValues[s[i]];
            } else {
                totalSum += romanValues[s[i]];
            }
        }
        
        return totalSum;
    }
};
