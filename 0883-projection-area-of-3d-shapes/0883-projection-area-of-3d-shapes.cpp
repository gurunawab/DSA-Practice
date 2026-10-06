class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int ans = 0, n = grid.size();
        for (int i = 0; i < n; i++) {
            int rowMax = 0, colMax = 0;
            for (int j = 0; j < n; j++) {
                ans += grid[i][j] > 0;
                rowMax = max(rowMax, grid[i][j]);
                colMax = max(colMax, grid[j][i]);
            }
            ans += rowMax + colMax;
        }
        return ans;
    }
};