class Solution {
public:
    int scoreOfParentheses(string s) {
        int ans = 0, depth = 0;
        for (int i = 0; i < s.size(); ++i) {
            depth += (s[i] == '(' ? 1 : -1);
            if (s[i] == ')' && s[i - 1] == '(') ans += 1 << depth;
        }
        return ans;
    }
};