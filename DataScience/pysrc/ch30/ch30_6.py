# ch30_6.py
import sympy as sp
from sympy.plotting import plot

x = sp.Symbol('x')
f1 = sp.sin(x)
f2 = sp.cos(x)
line = plot(f1,f2,(x,0,2*sp.pi),legend=True,show=False)
line[1].line_color = 'g'
line.show()










