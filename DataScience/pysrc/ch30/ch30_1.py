# ch30_1.py
import sympy as sp

x = sp.Symbol('x')
f = 3*x**2 + 2*x + 10
print("f'(x) = ", f.diff())
print("f'(x) = ", sp.diff(f, x))
print("-"*50)
print("f''(x) = ", sp.diff(f, x, 2))



















