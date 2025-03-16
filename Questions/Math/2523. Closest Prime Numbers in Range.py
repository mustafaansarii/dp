from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Use Sieve of Eratosthenes to find all primes in range
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right + 1, i):
                    sieve[j] = False

        # Get list of primes in range
        primes = [i for i in range(max(2,left), right + 1) if sieve[i]]

        if len(primes) < 2:
            return [-1, -1]

        # Find closest pair
        min_diff = float('inf')
        min_pair = [-1, -1]
        for i in range(len(primes)-1):
            diff = primes[i+1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                min_pair = [primes[i], primes[i+1]]
        return min_pair


if __name__ == "__main__":
    s = Solution()
    left = 10
    right = 19
    Output= [11, 13]
    print(s.closestPrimes(left, right))