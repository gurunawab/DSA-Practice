class Solution {
public:
    int minInsertions(string s) {
        int ans = 0, need = 0;
        for (char c : s) {
            if (c == '(') {
                if (need % 2) { ans++; need--; }
                need += 2;
            } else if (--need < 0) {
                ans++;
                need += 2;
            }
        }
        return ans + need;
    }
};