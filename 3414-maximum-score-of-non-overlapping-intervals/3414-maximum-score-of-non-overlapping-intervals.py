from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
      
        A = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        N = len(A)
        starts = [x[0] for x in A]

        
        memo = {}

        def solve(i, count):
            if count == 0 or i == N:
                return (0, ())
            if (i, count) in memo:
                return memo[(i, count)]

           
            res = solve(i + 1, count)

           
            next_idx = bisect_right(starts, A[i][1])
            w_take, idxs_take = solve(next_idx, count - 1)
            take_res = (A[i][2] + w_take, (A[i][3],) + idxs_take)

            
            if take_res[0] > res[0] or (take_res[0] == res[0] and sorted(take_res[1]) < sorted(res[1])):
                res = take_res

            memo[(i, count)] = res
            return res

        return list(sorted(solve(0, 4)[1]))