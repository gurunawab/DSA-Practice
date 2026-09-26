#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return 0;

        std::unordered_set<std::string> beginSet = {beginWord}, endSet = {endWord};
        int len = 1;

        while (!beginSet.empty() && !endSet.empty()) {
            if (beginSet.size() > endSet.size()) std::swap(beginSet, endSet);
            std::unordered_set<std::string> nextSet;

            for (std::string word : beginSet) {
                for (int i = 0; i < word.length(); ++i) {
                    char orig = word[i];
                    for (char c = 'a'; c <= 'z'; ++c) {
                        word[i] = c;
                        if (endSet.count(word)) return len + 1;
                        if (dict.erase(word)) nextSet.insert(word);
                    }
                    word[i] = orig;
                }
            }
            beginSet = std::move(nextSet);
            len++;
        }
        return 0;
    }
};