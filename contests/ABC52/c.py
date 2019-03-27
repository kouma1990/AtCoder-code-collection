n = int(input())

# 素因数分解
import math
import random


class Prime:
    seed_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_prime(self, n):
        """
        prime test (hybrid)

        see also: https://qiita.com/gushwell/items/ff9ed83ba55350aaa369

        :param n:
        :return: boolean
        """
        is_prime_common = self.is_prime_common(n)
        if is_prime_common is not None:
            return is_prime_common

        if n < 2000000:
            return self.is_prime_brute_force(n)
        else:
            return self.is_prime_miller_rabin(n)

    def is_prime_common(self, n):
        if n == 1: return False
        if n in Prime.seed_primes: return True
        if any(map(lambda x: n % x == 0, self.seed_primes)): return False

    def is_prime_brute_force(self, n):
        """
        brute force prime test
        use with is_prime_common if you want to skip seed_primes

        :param n:
        :return: boolean
        """
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True

    def is_prime_miller_rabin(self, n):
        """
        miller rabin prime test
        use with is_prime_common if you want to skip seed_primes

        see also
            algorithm: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
            implementation: https://qiita.com/srtk86/items/609737d50c9ef5f5dc59
            improvement: https://qiita.com/gushwell/items/ff9ed83ba55350aaa369

        :param n:
        :return: boolean
        """

        d = n - 1
        while d & 1 == 0:
            d >>= 1

        # use one of these lines / upper is more efficient.
        witnesses = self.get_witnesses(n)
        # witnesses = [random.randint(1, n - 1) for _ in range(100)]

        for w in witnesses:
            y = pow(w, d, n)

            while d != n - 1 and y != 1 and y != n - 1:
                y = (y * y) % n
                d <<= 1

            if y != n - 1 and d & 1 == 0:
                return False

        return True

    def get_witnesses(self, num):
        def _get_range(num):
            if num < 2047:
                return 1
            if num < 1373653:
                return 2
            if num < 25326001:
                return 3
            if num < 3215031751:
                return 4
            if num < 2152302898747:
                return 5
            if num < 3474749660383:
                return 6
            if num < 341550071728321:
                return 7
            if num < 3825123056546413051:
                return 9
            return 12

        return self.seed_primes[:_get_range(num)]

    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        if b == 0:
            return a
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def f(x, n, seed):
        """
        pseudo prime generator
        :param x:
        :param n:
        :param seed:
        :return: pseudo prime
        """
        p = Prime.seed_primes[seed % len(Prime.seed_primes)]
        return (p * x + seed) % n

    def find_factor(self, n, seed=1):
        """
        find one of factor of n
        this function is based to Pollard's rho algorithm

        see also
            algorithm: https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
            implementation: https://qiita.com/gushwell/items/561afde2e00bf3380c98

        :param n:
        :param seed:
        :return: factor
        """
        if self.is_prime(n):
            return n

        x, y, d = 2, 2, 1
        count = 0
        while d == 1:
            count += 1
            x = self.f(x, n, seed)
            y = self.f(self.f(y, n, seed), n, seed)
            d = self.gcd(abs(x - y), n)

        if d == n:
            return self.find_factor(n, seed+1)
        return self.find_factor(d)

    def find_factors(self, n):
        primes = {}
        if self.is_prime(n):
            primes[n] = 1
            return primes

        while n > 1:
            factor = self.find_factor(n)

            primes.setdefault(factor, 0)
            primes[factor] += 1

            n //= factor

        return primes


prime = Prime()
cnt = [0]*(n+1)
for i in range(2,n+1):
    for x,c in prime.find_factors(i).items():
        cnt[x] += c
    
res = 1
for x in cnt:
    res *= (x+1)

print(res%(10**9+7))
