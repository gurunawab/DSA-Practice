from collections import Counter

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = Counter(f for f, _ in items)
        
        mult_cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                for m in range(f, n + 1, f):
                    mult_cnt[f] += freq[m]
                    
        items.sort(key=lambda x: x[1])
        min_price = items[0][1]
        total_items = 0
        
        for f, p in items:
            # Agar 2-for-1 deal ka price 2 cheapest items se zyada ya barabar hai, toh ruk jao
            if p >= 2 * min_price or budget < p:
                break
                
            max_free = mult_cnt[f] - 1
            if max_free <= 0:
                continue
            
            buy = min(max_free, budget // p)
            total_items += buy * 2
            budget -= buy * p
                
        return total_items + budget // min_price