import numpy as np
from sklearn.linear_model import LinearRegression
from prime_patt import sieve

primes = sieve(1_000_000)

n_values = np.arange(1, len(primes) + 1)
prime_values = np.array(primes)

X = np.column_stack([n_values, n_values * np.log(n_values + 1)])
y = prime_values

split = int(len(primes) * 0.8)
Xtr, Xte = X[:split], X[split:]
ytr, yte = y[:split], y[split:]

model = LinearRegression().fit(Xtr, ytr)
pred = model.predict(Xte)

formula_est = n_values[split:] * np.log(n_values[split:])
model_err   = np.mean(np.abs(pred - yte) / yte) * 100
formula_err = np.mean(np.abs(formula_est - yte) / yte) * 100

print(f"Formula (n·ln n) error: {formula_err:.2f}%")
print(f"Model error:            {model_err:.2f}%")
# Check: does it hold across the whole test range, or just on average?
errors = np.abs(pred - yte) / yte * 100
print(f"Mean error:  {errors.mean():.3f}%")
print(f"Worst error: {errors.max():.3f}%")
print(f"Best error:  {errors.min():.3f}%")
print("Coefficients:", model.coef_)
print("Intercepts:",model.intercept_)