from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
from task2_prereq import primes, gaps

# Features: things known BEFORE the next prime - position, current prime size, recent gaps
n_idx = np.arange(1, len(gaps))
X = np.column_stack([
    n_idx,                          # position
    np.log(primes[:-1][1:] ),       # log of current prime
    gaps[:-1]                       # the PREVIOUS gap
])
y = gaps[1:]                        # predict the NEXT gap

split = int(len(X) * 0.8)
Xtr, Xte = X[:split], X[split:]
ytr, yte = y[:split], y[split:]

model = LinearRegression().fit(Xtr, ytr)
pred = model.predict(Xte)

r2 = r2_score(yte, pred)
print(f"R² score: {r2:.4f}")
print(f"Mean actual gap: {yte.mean():.2f}")
print(f"Mean predicted gap: {pred.mean():.2f}")
print(f"Sample predictions: {pred[:8].round(1)}")
print(f"Actual values:      {yte[:8]}")