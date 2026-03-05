#Isomorphic String
def Isomorphic(self, s1, s2):

    if len(s1) != len(s2):
        return False
    
    mapST = {}
    mapTS = {}

    for char1, char2 in zip(s1, s2):
        if char1 in mapST:
            if mapST[char1] != char2:
                return False
            
        if char2 in mapTS:
            if mapTS[char2] != char1:
                return False

        mapST[char1] = char2
        mapTS[char2] = char1

    return True

#Number of steps to Reduce a Number
def numSteps(self, s):
    steps = 0
    carry = 0

    for i in range(len(s)-1, 0, -1):
        
        if int(s[i]) + carry == 1:
            steps += 2
            carry = 1
        else:
            carry += 1

    return steps + carry

#Number of SUbmatrix have sum X
def countSquare(mat, x):
    n = len(mat)
    m = len(mat[0])

    pref = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = (mat[i-1][j-1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1])

    count = 0

    max_k = min(n, m)
    for k in range(1, max_k + 1):
        for i in range(k, n + 1):
            for j in range(k, m + 1):
                current_sum = (pref[i][j] - pref[i-k][j] - pref[i][j-k] + pref[i-k][j-k])

                if current_sum == x:
                    count += 1

    return count                        


#Minimum operations to Equalize Binary String
from collections import deque

class Sloution(object):
    def minOperations(self, s, k):
        n = len(s)
        start_zeros = s.coutn('0')

        if start_zeros == 0:
            return 0
        
        queue = deque([(start_zeros, 0)])
        visited = {start_zeros}

        while queue:
            z, steps = queue.popleft()

            min_i = max(0, k - (n-z))
            max_i = min(z, k)

            for i in range(min_i, min_i + 1):
                next_z = z - i + (k - i)

                if next_z == 0:
                    return steps + 1
                
                if next_z not in visited:
                    visited.add(next_z)
                    queue.append((next_z, steps + 1))

        return -1

#find the closest pair from two arrays
def findClosestPair(arr1, arr2, x):
    n = len(arr1)
    m = len(arr2)

    left = 0
    right = m - 1

    min_diff = float('inf')
    res = []

    while left < n and right >= 0:
        current_sum = arr1[left] + arr2[right]

        current_diff = abs(current_sum - x)

        if current_diff < min_diff:
            min_diff = current_diff
            res = [arr1[left], arr2[right]]

        if current_sum > x:
            right -= 1
        else:
            left += 1

    return res    

# Concatenation of Consecutive Binary Numbers
def concatenatedBinary(self, n):
    MOD = 10**9 + 7
    result = 0
    length = 0

    for i in range(1, n + 1):
        if (i &(i - 1)) == 0:
            length += 1

        result = ((result << length) + i) % MOD

    return result

#Move all Zeros to end
def pushZerosToEnd(self, arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

    return arr                                                   

         