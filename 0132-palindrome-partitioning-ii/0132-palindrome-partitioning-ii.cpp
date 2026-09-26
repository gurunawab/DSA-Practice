#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

class Solution {
public:
    int minCut(std::string s) {
        int n = s.length();
        std::vector<int> cuts(n + 1);
        std::iota(cuts.begin(), cuts.end(), -1); // Initialize cuts[i] = i - 1

        for (int i = 0; i < n; ++i) {
            // Odd length palindromes (center at i)
            for (int l = 0; i - l >= 0 && i + l < n && s[i - l] == s[i + l]; ++l)
                cuts[i + l + 1] = std::min(cuts[i + l + 1], cuts[i - l] + 1);

            // Even length palindromes (center between i and i+1)
            for (int l = 0; i - l >= 0 && i + 1 + l < n && s[i - l] == s[i + 1 + l]; ++l)
                cuts[i + 2 + l] = std::min(cuts[i + 2 + l], cuts[i - l] + 1);
        }

        return cuts[n];
    }
};