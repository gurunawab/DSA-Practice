class Solution {
public:
    int totalNQueens(int n, int cols = 0, int diag1 = 0, int diag2 = 0) {
        if (cols == (1 << n) - 1) return 1;
        int count = 0, available = ((1 << n) - 1) & ~(cols | diag1 | diag2);
        while (available) {
            int bit = available & -available;
            count += totalNQueens(n, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1);
            available &= available - 1;
        }
        return count;
    }
};