import numpy as np

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

primes = sieve(1_000_000)

for n in [10, 100, 1000, 10000, 78498]:
    actual = primes[n-1]
    estimate = n * np.log(n)
    error = (estimate - actual) / actual * 100
    print(f"n={n:>6}: actual={actual:>9}, n·ln(n)={estimate:>12.0f}, error={error:+.1f}%")