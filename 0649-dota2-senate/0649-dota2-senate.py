class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_q = deque(i for i, s in enumerate(senate) if s == 'R')
        d_q = deque(i for i, s in enumerate(senate) if s == 'D')
        
        while r_q and d_q:
            r, d = r_q.popleft(), d_q.popleft()
            if r < d:
                r_q.append(r + n)
            else:
                d_q.append(d + n)
                
        return "Radiant" if r_q else "Dire"