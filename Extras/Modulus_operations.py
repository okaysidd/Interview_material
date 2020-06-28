"""
For creating own rolling hash, we use modulus to prevent overflowing.
If adding/multiplying numbers results in overflow:
(a + b) % m = ((a % m) + (b % m)) % m
(a * b) % m = ((a % m) * (b % m)) % m
(a / b) % m = (a * inverse of b) % m
"""
