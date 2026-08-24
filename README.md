# Prime Prediction

An empirical study of which properties of prime numbers are learnable by
machine learning — and which are not.

## The idea

I wanted to see whether machine learning could find a pattern in prime numbers —
interesting precisely because primes are famous for having no simple pattern.
The result split in two: I could predict the value of the nth prime to within
0.03% error, but the gaps between consecutive primes couldn't be predicted at
all. That contrast — one thing highly predictable, the other essentially random —
turned out to be the real finding.

## Results

Trained on primes up to 1,000,000 (~78,000 primes), using scikit-learn:

| Task | What it predicts | Result |
|------|------------------|--------|
| **1** | Value of the nth prime | **0.03% error** — near perfect |
| **2** | Gap to the next prime | **R² ≈ 0.004** — no better than guessing the average |

Same data, same tools — one task succeeds spectacularly, the other fails
completely. That contrast is the finding.

## Task 1 — predicting the nth prime (learnable)

The Prime Number Theorem gives a crude estimate, `n·ln(n)`, which undershoots
by ~11–20%. A linear model given `n` and `n·ln(n)` as features learned the
correction, producing:

    p(n) ≈ 0.4107·n + 1.0937·(n·ln n) − 66.49

- 0.03% error in the training range
- Holds under 0.2% error even when extrapolated 10× beyond it (tested to ~10M)

The model found a linear relation between the inputs (`n`, `n·ln(n)`) and the
actual nth prime that minimized the error dramatically — mean error 0.03%, best
case essentially zero, worst case 0.07%. This closes almost the entire gap left
by the crude `n·ln(n)` formula (which was ~11.5% off), bringing the accuracy
roughly to the level of the logarithmic integral, the approximation
mathematicians actually use.

This is a *rediscovery* of known mathematics, not a new formula — the model
independently arrived at the correction that number theory already describes.
What I found interesting was watching the linear relation hold, then slowly
break down: extrapolated far beyond the training range, the error creeps up,
showing the limit of a fixed linear correction on a relationship that keeps
subtly shifting.

## Task 2 — predicting prime gaps (not learnable)

When the model tried to predict the *gap* to the next prime — using the
position, the current prime's size, and the previous gap — it failed almost
completely. The R² was about 0.004, meaning it explained essentially none of
the variation. In practice it gave up and just predicted the average gap (~13)
for almost everything, while the real gaps swung wildly (4, 24, 6, 8...).
Predicting the mean is the safest guess when there's no pattern to learn — and
that's exactly what the model fell back on.

This makes sense. The smooth *trend* in how primes thin out is learnable
(that's Task 1), but the exact spacing between individual primes is erratic.
This isn't just my model being weak — the "thickening and thinning" of primes
is, as far as mathematics knows, governed by the zeros of the Riemann zeta
function, the deepest unsolved problem in the field. If a simple model could
predict prime gaps, it would be solving something centuries of number theory
hasn't.

## What this demonstrates

Putting the two tasks together: the overall *density* of primes is highly
predictable, but the *exact gap* between one prime and the next is not. The same
data and the same tools give a near-perfect result on one task and a
near-useless one on the other — and that boundary between what's learnable and
what isn't is the real finding.

One honest caveat: Task 2 shows the gaps are unpredictable *from these features,
with this model*. That's consistent with the deep result that prime gaps have no
known simple pattern — but a single failed experiment illustrates that, it
doesn't prove it.

## Running it

    python task1.py    # nth-prime prediction
    python task2.py    # prime-gap prediction

## Limitations & honest notes

- Task 1's formula is a rediscovery of known approximations (logarithmic
  integral territory), not new mathematics
- Task 1 is fitted to a range; it drifts if extrapolated far enough
- Task 2's null result illustrates, but does not prove, the unpredictability
  of prime gaps