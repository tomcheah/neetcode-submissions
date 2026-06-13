class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n

        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, n):
            if is_prime[i]:
                multiple = i*i
                while multiple < n:
                    is_prime[multiple] = False
                    multiple += i

        return sum(is_prime)