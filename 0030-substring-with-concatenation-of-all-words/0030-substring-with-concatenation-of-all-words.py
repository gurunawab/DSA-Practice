from collections import Counter


class Solution:

  def findSubstring(self, s: str, words: list[str]) -> list[int]:
    word_len, total_len = len(words[0]), len(words) * len(words[0])
    word_counts = Counter(words)

    res = []
    for i in range(len(s) - total_len + 1):
      sub = s[i : i + total_len]
      seen = Counter(
          sub[j : j + word_len] for j in range(0, total_len, word_len)
      )
      if seen == word_counts:
        res.append(i)

    return res