import numpy as np
from prime_patt import sieve

# Your learned formula
def my_formula(n):
    return 0.41068517*n + 1.0936794*(n*np.log(n)) - 66.48951419

# Generate primes further than training range
big_primes = sieve(10_000_000)   # ~348k primes, well beyond the 1M training

# Test at positions BEYOND what you trained on (you trained up to ~78,498th prime)
for n in [100_000, 200_000, 300_000, 348_000, 400_000, 500_000, len(big_primes)]:
    if n <= len(big_primes):
        actual = big_primes[n-1]
        pred = my_formula(n)
        err = (pred - actual) / actual * 100
        print(f"n={n:>7}: actual={actual:>9}, formula={pred:>12.0f}, error={err:+.3f}%")