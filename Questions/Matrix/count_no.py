class Solution:
    def countNumbers(self, l, r):
        MOD = 10 ** 9 + 7

        def count_odd(x):
            if x < 0:
                return 0
            s = bin(x)[2:]
            n = len(s)
            from functools import lru_cache

            @lru_cache(None)
            def dp(pos, tight, parity):
                if pos == n:
                    return 1 if parity == 1 else 0
                res = 0
                limit = int(s[pos]) if tight else 1
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    new_parity = (parity + d) % 2
                    res += dp(pos + 1, new_tight, new_parity)
                return res

            return dp(0, True, 0)

        return (count_odd(r) - count_odd(l - 1)) % MOD