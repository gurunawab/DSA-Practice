class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.empty()) return 0;
        vector<int> buy(k + 1, INT_MIN), sell(k + 1, 0);

        for (int p : prices) {
            for (int i = 1; i <= k; ++i) {
                buy[i] = max(buy[i], sell[i - 1] - p);
                sell[i] = max(sell[i], buy[i] + p);
            }
        }
        return sell[k];
    }
};