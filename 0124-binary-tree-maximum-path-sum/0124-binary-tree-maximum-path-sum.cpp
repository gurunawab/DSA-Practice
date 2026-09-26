/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <algorithm>
#include <climits>

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;

        auto dfs = [&](auto& self, TreeNode* node) -> int {
            if (!node) return 0;
            int left = std::max(0, self(self, node->left));
            int right = std::max(0, self(self, node->right));
            maxSum = std::max(maxSum, node->val + left + right);
            return node->val + std::max(left, right);
        };

        dfs(dfs, root);
        return maxSum;
    }
};