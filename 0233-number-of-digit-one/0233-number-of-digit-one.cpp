class Solution {
public:
    int countDigitOne(int n) {
        long long ans = 0;
        for (long long m = 1; m <= n; m *= 10)
            ans += (n / (m * 10)) * m + min(max(n % (m * 10) - m + 1, 0LL), m);
        return ans;
    }
};