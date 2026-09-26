#include <string>

class Solution {
public:
    bool isNumber(std::string s) {
        bool seenDigit = false, seenDot = false, seenE = false;

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (isdigit(c)) seenDigit = true;
            else if (c == '+' || c == '-') {
                if (i > 0 && s[i - 1] != 'e' && s[i - 1] != 'E') return false;
            } else if (c == 'e' || c == 'E') {
                if (seenE || !seenDigit) return false;
                seenE = true;
                seenDigit = false;
            } else if (c == '.') {
                if (seenDot || seenE) return false;
                seenDot = true;
            } else return false;
        }

        return seenDigit;
    }
};