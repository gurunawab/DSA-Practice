#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int buy1 = INT_MAX, buy2 = INT_MAX;
        int sell1 = 0, sell2 = 0;

        for (int price : prices) {
            buy1 = std::min(buy1, price);
            sell1 = std::max(sell1, price - buy1);
            buy2 = std::min(buy2, price - sell1);
            sell2 = std::max(sell2, price - buy2);
        }

        return sell2;
    }
};