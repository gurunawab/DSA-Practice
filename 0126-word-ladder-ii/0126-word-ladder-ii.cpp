#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    std::vector<std::vector<std::string>> findLadders(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return {};

        std::unordered_map<std::string, int> dist;
        std::unordered_map<std::string, std::vector<std::string>> parents;
        std::vector<std::string> q = {beginWord};
        dist[beginWord] = 0;

        int head = 0;
        bool found = false;

        while (head < q.size() && !found) {
            int size = q.size() - head;
            for (int k = 0; k < size; ++k) {
                std::string u = q[head++];
                std::string v = u;

                for (int i = 0; i < v.length(); ++i) {
                    char orig = v[i];
                    for (char c = 'a'; c <= 'z'; ++c) {
                        v[i] = c;
                        if (dict.count(v)) {
                            if (!dist.count(v)) {
                                dist[v] = dist[u] + 1;
                                q.push_back(v);
                                parents[v].push_back(u);
                                if (v == endWord) found = true;
                            } else if (dist[v] == dist[u] + 1) {
                                parents[v].push_back(u);
                            }
                        }
                    }
                    v[i] = orig;
                }
            }
        }

        std::vector<std::vector<std::string>> res;
        std::vector<std::string> path = {endWord};

        auto dfs = [&](auto& self, const std::string& node) -> void {
            if (node == beginWord) {
                res.push_back({path.rbegin(), path.rend()});
                return;
            }
            for (const auto& p : parents[node]) {
                path.push_back(p);
                self(self, p);
                path.pop_back();
            }
        };

        if (found) dfs(dfs, endWord);
        return res;
    }
};