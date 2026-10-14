#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#include <string>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> bracketStack;
        
        for (char c : s) {
            if (c == '(') {
                bracketStack.push(')');
            } else if (c == '{') {
                bracketStack.push('}');
            } else if (c == '[') {
                bracketStack.push(']');
            } else {
                // If it's a closing bracket, check stack validity and matching
                if (bracketStack.empty() || bracketStack.top() != c) {
                    return false;
                }
                bracketStack.pop();
            }
        }
        
        // If stack is empty, all brackets were correctly matched and closed
        return bracketStack.empty();
    }
};
