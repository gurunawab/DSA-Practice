class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> mask;
        for (auto& r : reservedSeats)
            if (r[1] >= 2 && r[1] <= 9)
                mask[r[0]] |= (1 << (r[1] - 2));

        int ans = (n - mask.size()) * 2;
        for (auto& [_, m] : mask) {
            bool left = !(m & 0b00001111);   // seats 2, 3, 4, 5
            bool right = !(m & 0b11110000);  // seats 6, 7, 8, 9
            bool mid = !(m & 0b00111100);    // seats 4, 5, 6, 7
            
            if (left && right) ans += 2;
            else if (left || right || mid) ans += 1;
        }
        return ans;
    }
};