#include <vector>
#include <map>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int maxPoints(std::vector<std::vector<int>>& points) {
        int n = points.size();
        if (n <= 2) return n;

        int max_pts = 1;

        for (int i = 0; i < n; ++i) {
            std::map<std::pair<int, int>, int> slope_map;

            for (int j = i + 1; j < n; ++j) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                int g = std::gcd(dx, dy);
                dx /= g;
                dy /= g;

                // Force dx to be positive to normalize direction
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }

                slope_map[{dx, dy}]++;
                max_pts = std::max(max_pts, slope_map[{dx, dy}] + 1);
            }
        }

        return max_pts;
    }
};