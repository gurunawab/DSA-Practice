#include <vector>
#include <algorithm>

class Solution {
public:
    int uniqueXorTriplets(std::vector<int>& nums) {
       
        std::vector<int> S = nums;
        std::sort(S.begin(), S.end());
        S.erase(std::unique(S.begin(), S.end()), S.end());

        int n = S.size();
        bool seen[2048] = {false};
        int unique_count = 0;

        
        for (int val : S) {
            if (!seen[val]) {
                seen[val] = true;
                unique_count++;
            }
        }

        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int pair_xor = S[i] ^ S[j];
                for (int k = j + 1; k < n; ++k) {
                    int triplet_xor = pair_xor ^ S[k];
                    if (!seen[triplet_xor]) {
                        seen[triplet_xor] = true;
                        unique_count++;
                        
                        if (unique_count == 2048) {
                            return 2048;
                        }
                    }
                }
            }
        }

        return unique_count;
    }
};