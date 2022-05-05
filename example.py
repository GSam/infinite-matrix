import pdb
import symengine
import sympy
import pprint
from riordan.matrix import *

#(Pdb) symengine.series((ra).gmul(symengine.sympify('(1+x-(1-2*x-3*x**2)**(1/2)) / 2x')), n = 10)
#1 + 2*x + 4*x**2 + 9*x**3 + 23*x**4 + 65*x**5 + 197*x**6 + 626*x**7 + 2056*x**8
#(Pdb) symengine.series((iden).gmul(symengine.sympify('(1-(1-4*x)**(1/2)) / 2x')), n = 10)
#1 + x + 2*x**2 + 5*x**3 + 14*x**4 + 42*x**5 + 132*x**6 + 429*x**7 + 1430*x**8
#(Pdb) symengine.series((ones).gmul(symengine.sympify('(1-(1-4*x)**(1/2)) / 2x')), n = 10)

# 
motzkin = RiordanArray(sympy.sympify('1'),
                       sympy.sympify('(1-x-(1-2*x-3*x**2)**(1/2)) / 2*x**2'))

iden = RiordanArray(sympy.sympify('1'),
                    sympy.sympify('x'))

# Shift Right
single = RiordanArray(sympy.sympify('x'),
                      sympy.sympify('x'))

# Shift Left
anti = RiordanArray(sympy.sympify('x'),
                      sympy.sympify('1'))

# Aeration
double = RiordanArray(sympy.sympify('1'),
                      sympy.sympify('x**2'))

# Partial Sum - A(z) / (1 - z)
ones = RiordanArray(sympy.sympify('1/(1-x)'),
                    sympy.sympify('x'))

# Difference - (1 - z) . A(z)
invert_ones = RiordanArray(sympy.sympify('1-x'),
                    sympy.sympify('x'))

invert_fib = RiordanArray(sympy.sympify('1'),
                          sympy.sympify('x**2 + x'))

# Partial Sum x Right = B
ra = RiordanArray(sympy.sympify('1/(1-x)'),
                  sympy.sympify('x/(1-x)'))

fb = RiordanArray(sympy.sympify('1/(1-x-x**2)'),
                  sympy.sympify('(1-(1-4*x)**(1/2)) / 2'))

right = RiordanArray(sympy.sympify('1'),
                    sympy.sympify('x/(1-x)'))

# Left x Difference = B ** -1
# Right ** -1 x Partial Sum ** -1  = B ** -1
invert_b = RiordanArray(sympy.sympify('1/(1+x)'),
                        sympy.sympify('x/(1+x)'))


import sympy as sy
#from sympy.functions.combinatorial.factorials import factorial

# Factorial function
import functools

@functools.lru_cache(maxsize=100)
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

# Taylor approximation at x0 of the function 'function'
def taylor(function, x0, n, x = symengine.Symbol('x')):
    i = 0
    p = 0

    current = function
    while i <= n:
        #current = function.diff(x, i)
        temp = current.subs(x, x0)
        temp2 = temp / (factorial(i))*(x - x0)**i
        p = p + temp2
        i += 1
        current = current.diff()
    return p

#print(taylor(symengine.sympify('1/(1-x-x^2)'), 0, 20))

# Taylor approximation at x0 of the function 'function'
def taylor2(function, x0, n, x = symengine.Symbol('x')):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, x0))/(factorial(i))*(x - x0)**i
        i += 1
    return p

def taylor3(function, x0, n, x = symengine.Symbol('x')):
    i = 0
    p = 0
    while i <= n:
        temp = function.diff(x, i)
        p = p + (temp.subs(x, x0))/(factorial(i))*(x - x0)**i
        i += 1
        print(i)
    return p

pprint.pprint(ra.matrix(3))
pprint.pprint((ra * fb).matrix(10))

import pdb
pdb.set_trace()
#ra.get(1,1)
#pdb.set_trace()

#print(taylor3(symengine.sympify('1/(1-x-x^2)'), 0, 20))
