class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0, add = 0;
        for (char c : s) {
            if (c == '(') open++;
            else open ? open-- : add++;
        }
        return open + add;
    }
};