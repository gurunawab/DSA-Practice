class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        sorted_freqs = sorted(freq.values(), reverse=True)

        ans = 0
        for i, count in enumerate(sorted_freqs):
            pushes = (i // 8) + 1
            ans += count * pushes
            
        return ans