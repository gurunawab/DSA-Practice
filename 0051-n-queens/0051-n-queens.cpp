#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::vector<std::string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> res;
        std::vector<std::string> board(n, std::string(n, '.'));
        std::vector<bool> cols(n, false), diag1(2 * n, false), diag2(2 * n, false);

        auto backtrack = [&](auto& self, int r) -> void {
            if (r == n) {
                res.push_back(board);
                return;
            }
            for (int c = 0; c < n; ++c) {
                if (cols[c] || diag1[r + c] || diag2[r - c + n]) continue;
                board[r][c] = 'Q';
                cols[c] = diag1[r + c] = diag2[r - c + n] = true;

                self(self, r + 1);

                board[r][c] = '.';
                cols[c] = diag1[r + c] = diag2[r - c + n] = false;
            }
        };

        backtrack(backtrack, 0);
        return res;
    }
};