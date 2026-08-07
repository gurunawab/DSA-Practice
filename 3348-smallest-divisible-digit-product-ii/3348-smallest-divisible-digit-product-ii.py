class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        
        c = [0] * 4
        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                c[i] += 1
                t //= p
        if t > 1:
            return "-1"

       
        def get_digits(c2, c3, c5, c7):
            c2, c3, c5, c7 = max(0, c2), max(0, c3), max(0, c5), max(0, c7)
            d9, c3 = divmod(c3, 2)
            d8, c2 = divmod(c2, 3)
            d2 = d3 = d4 = d6 = 0
            if c3 and c2 == 2: d2 = d6 = 1
            elif c3 and c2 == 1: d6 = 1
            elif c3: d3 = 1
            elif c2 == 2: d4 = 1
            elif c2 == 1: d2 = 1
            return '2'*d2 + '3'*d3 + '4'*d4 + '5'*c5 + '6'*d6 + '7'*c7 + '8'*d8 + '9'*d9

        F = {1: (0,0,0,0), 2: (1,0,0,0), 3: (0,1,0,0), 4: (2,0,0,0), 
             5: (0,0,1,0), 6: (1,1,0,0), 7: (0,0,0,1), 8: (3,0,0,0), 9: (0,2,0,0)}

        n = len(num)
        z = num.find('0')
        limit = z if z != -1 else n

        
        pref = [[0] * 4]
        for ch in num[:limit]:
            pref.append([p + q for p, q in zip(pref[-1], F[int(ch)])])

        
        for i in range(limit, -1, -1):
            p_c = pref[i]
            if i == n:
                if all(p_c[j] >= c[j] for j in range(4)):
                    return num
                continue

            start_d = 1 if i == z else int(num[i]) + 1
            for d in range(start_d, 10):
                rem_slots = n - 1 - i
                req = [c[j] - p_c[j] - F[d][j] for j in range(4)]
                s = get_digits(*req)
                if len(s) <= rem_slots:
                    return num[:i] + str(d) + '1' * (rem_slots - len(s)) + s

      
        s = get_digits(*c)
        target_len = max(n + 1, len(s))
        return '1' * (target_len - len(s)) + s