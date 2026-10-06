class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<bool> isPrime(right + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (long long i = 2; i * i <= right; i++)
            if (isPrime[i])
                for (long long j = i * i; j <= right; j += i) isPrime[j] = false;

        vector<int> primes;
        for (int i = max(2, left); i <= right; i++)
            if (isPrime[i]) primes.push_back(i);

        vector<int> ans = {-1, -1};
        int minDiff = 1e9;
        for (int i = 1; i < primes.size(); i++) {
            if (primes[i] - primes[i - 1] < minDiff) {
                minDiff = primes[i] - primes[i - 1];
                ans = {primes[i - 1], primes[i]};
                if (minDiff <= 2) break;
            }
        }
        return ans;
    }
};