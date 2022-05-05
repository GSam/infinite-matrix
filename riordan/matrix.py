import symengine
import math
from sympy import Poly, factorial
import functools
import numpy as np
import traceback

class Matrix:
    pass

class RiordanArray(Matrix):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    '''Use the standard method for fetching against a Riordan array.

    [row] left * right ^ col

    '''
    @functools.lru_cache(maxsize=None)
    def get(self, row, col, x=symengine.symbols('x')):

        # Row and columns start from 1
        gf = self.left * self.right ** (col - 1)

        expansion = symengine.series(gf, x, n=row)

        if expansion.is_Number:
            return int(expansion)

        return Poly(expansion).all_coeffs()[0]

    def matrix(self, n, m=None, x=symengine.symbols('x')):
        result = []
        # Square matrix by default
        if not m:
            m = n

        for col in range(n):

            # Row and columns start from 1
            gf = self.left * self.right ** col

            expansion = symengine.series(gf, x, n=n)

            if expansion.is_Number:
                filler = (n-1) * [0]
                result.append(filler+ [int(expansion)])
            else:
                coeff = Poly(expansion).all_coeffs()
                filler = [0] * (m - len(coeff))
                result.append(filler + coeff)
                print(len(coeff), filler + coeff, m, filler)


        print(result)
        result = np.array(result, dtype=int)
        return np.rot90(result)

    # (g, f).(u, v) = (g.u(f), v(f))
    def __mul__(self, other, x=symengine.symbols('x')):
        if not isinstance(other, RiordanArray):
            raise Exception('Not Riordan')

        left = self.left * other.left.subs(x, self.right)
        right = other.right.subs(x, self.right)

        return RiordanArray(left, right)

    rmul = __mul__

    # (g, f).u(x) = g.u(f)
    #
    # Essentially looks like:
    # (g, f).(u, 0) = (g.u(f), 0)
    def gmul(self, gf, x=symengine.symbols('x')):
        other = gf
        left = self.left * other.subs(x, self.right)

        return left

class ExponentialRiordanArray(RiordanArray):

    def matrix(self, n, m=None, x=symengine.symbols('x')):
        result = []
        # Square matrix by default
        if not m:
            m = n

        for col in range(n):

            # Row and columns start from 1
            gf = self.left * self.right ** col / factorial(col)
            print(gf)

            expansion = symengine.series(gf, x, n=n)
            print(expansion)

            if expansion.is_Number:
                filler = (n-1) * [0]
                result.append(filler+ [int(expansion)])
            else:
                coeff = Poly(expansion).all_coeffs()
                filler = [0] * (m - len(coeff))
                print(filler + coeff, 'BLAH')
                print([(math.factorial(m - (i+1)),i) for i,x in enumerate(filler+coeff)], 'NOPE')
                coeff2 = [x * factorial(m - (i+1)) for i,x in enumerate(filler+coeff)]
                print(coeff2, 'HAHA')
                result.append(coeff2)
                #print(len(coeff), filler + coeff, m, filler)

        print(result)
        result = np.array(result)
        return np.rot90(result)
