class Solution {
public:
    string getPermutation(int n, int k) {
        string s = "", ans = "";
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            s += to_string(i);
            fact *= i;
        }
        for (k--; n > 0; n--) {
            fact /= n;
            ans += s[k / fact];
            s.erase(k / fact, 1);
            k %= fact;
        }
        return ans;
    }
};