class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = 1e9, ans = 0;
        for (int p : prices) {
            min_price = min(min_price, p);
            ans = max(ans, p - min_price);
        }
        return ans;
    }
};