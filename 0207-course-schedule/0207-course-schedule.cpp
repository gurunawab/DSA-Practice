class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(n);
        vector<int> inDegree(n, 0), q;

        for (auto& p : prerequisites) {
            adj[p[1]].push_back(p[0]);
            inDegree[p[0]]++;
        }

        for (int i = 0; i < n; ++i)
            if (inDegree[i] == 0) q.push_back(i);

        for (int i = 0; i < q.size(); ++i) {
            for (int next : adj[q[i]]) {
                if (--inDegree[next] == 0) q.push_back(next);
            }
        }

        return q.size() == n;
    }
};