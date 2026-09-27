class Solution {
public:
    string reverseParentheses(string s) {
        vector<int> st;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') st.push_back(i);
            else if (s[i] == ')') {
                reverse(s.begin() + st.back(), s.begin() + i);
                st.pop_back();
            }
        }
        s.erase(remove_if(s.begin(), s.end(), [](char c) { return c == '(' || c == ')'; }), s.end());
        return s;
    }
};