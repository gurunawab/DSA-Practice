#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>

class Solution {
    std::unordered_map<std::string, std::vector<std::string>> memo;

public:
    std::vector<std::string> wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> dict(wordDict.begin(), wordDict.end());
        
        auto dfs = [&](auto& self, std::string str) -> std::vector<std::string> {
            if (memo.count(str)) return memo[str];
            if (str.empty()) return {""};

            std::vector<std::string> res;
            for (int i = 1; i <= str.length(); ++i) {
                std::string prefix = str.substr(0, i);
                if (dict.count(prefix)) {
                    for (const std::string& sub : self(self, str.substr(i))) {
                        res.push_back(prefix + (sub.empty() ? "" : " ") + sub);
                    }
                }
            }
            return memo[str] = res;
        };

        return dfs(dfs, s);
    }
};