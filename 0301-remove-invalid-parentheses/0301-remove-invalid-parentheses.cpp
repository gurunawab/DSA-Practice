class Solution {
    bool isValid(const string& s) {
        int cnt = 0;
        for (char c : s) {
            if (c == '(') cnt++;
            else if (c == ')' && --cnt < 0) return false;
        }
        return cnt == 0;
    }
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans;
        unordered_set<string> visited = {s};
        queue<string> q;
        q.push(s);
        bool found = false;

        while (!q.empty()) {
            string cur = q.front(); q.pop();
            if (isValid(cur)) {
                ans.push_back(cur);
                found = true;
            }
            if (found) continue;
            for (int i = 0; i < cur.size(); i++) {
                if (cur[i] != '(' && cur[i] != ')') continue;
                string next = cur.substr(0, i) + cur.substr(i + 1);
                if (visited.insert(next).second) q.push(next);
            }
        }
        return ans;
    }
};