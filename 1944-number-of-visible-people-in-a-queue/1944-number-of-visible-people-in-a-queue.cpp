class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int n = heights.size();
        vector<int> ans(n), st;
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && heights[i] > st.back()) {
                st.pop_back();
                ans[i]++;
            }
            if (!st.empty()) ans[i]++;
            st.push_back(heights[i]);
        }
        return ans;
    }
};