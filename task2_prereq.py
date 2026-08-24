import numpy as np
from prime_patt import sieve

primes = np.array(sieve(1_000_000))
gaps = np.diff(primes)      # gap[i] = primes[i+1] - primes[i]

print(f"Number of gaps: {len(gaps)}")
print(f"First 20 gaps: {gaps[:20]}")
print(f"Mean gap: {gaps.mean():.2f}")
print(f"Min gap: {gaps.min()}, Max gap: {gaps.max()}")