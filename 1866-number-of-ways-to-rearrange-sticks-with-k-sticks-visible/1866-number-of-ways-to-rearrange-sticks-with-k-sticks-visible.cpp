class Solution {
public:
    int rearrangeSticks(int n, int k) {
        vector<long long> dp(k + 1, 0);
        dp[1] = 1;
        for (int i = 2; i <= n; i++)
            for (int j = min(i, k); j >= 1; j--)
                dp[j] = (dp[j - 1] + (i - 1) * dp[j]) % 1000000007;
        return dp[k];
    }
};