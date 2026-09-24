from functools import cache


class Solution:

  def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)

    @cache
    def dfs(start: int) -> bool:
      if start == len(s):
        return True
      return any(
          s[start:end] in words and dfs(end)
          for end in range(start + 1, len(s) + 1)
      )

    return dfs(0)