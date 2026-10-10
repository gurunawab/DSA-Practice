class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int count[100001] = {}, k = k1 + k2;
        for (int i = 0; i < nums1.size(); ++i) 
            count[abs(nums1[i] - nums2[i])]++;
        
        for (int d = 100000; d > 0 && k > 0; --d) {
            int take = min(k, count[d]);
            count[d] -= take;
            count[d - 1] += take;
            k -= take;
        }

        long long ans = 0;
        for (long long d = 1; d <= 100000; ++d) 
            ans += (long long)count[d] * d * d;
        return ans;
    }
};