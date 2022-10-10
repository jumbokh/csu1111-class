# ch30_5.py
import sympy as sp
from sympy.plotting import plot

x = sp.Symbol('x')
f1 = 2*x-5
f2 = 3*x+2
line = plot(f1,f2,(x,-10,10),legend=True,show=False)
line[1].line_color = 'r'
line.show()









