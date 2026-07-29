from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        
        # Determine left half frequencies and middle character
        half_counts = [0] * 26
        mid = ""
        for char, freq in counts.items():
            half_counts[ord(char) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid = char
        
        half_len = sum(half_counts)
        
      
        def count_permutations(freq_list: list[int], cap: int) -> int:
            tot = sum(freq_list)
            res = 1
            # Multinomial coefficient calculation using nCr steps
            for f in freq_list:
                if f == 0:
                    continue
                res *= math.comb(tot, f)
                if res >= cap:
                    return cap
                tot -= f
            return res

        # Step 2: Check if k is greater than total possible distinct palindromic permutations
        total_perms = count_permutations(half_counts, k)
        if k > total_perms:
            return ""

        # Step 3: Construct the left half character by character
        left = []
        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                
                # Temporarily place character i at the current position
                half_counts[i] -= 1
                perms = count_permutations(half_counts, k)
                
                if perms >= k:
                    # Current character is valid at this position
                    left.append(chr(ord('a') + i))
                    break
                else:
                    # Target index lies past these permutations
                    k -= perms
                    half_counts[i] += 1  # Backtrack and try next character

        # Step 4: Assemble full palindrome
        left_str = "".join(left)
        return left_str + mid + left_str[::-1]