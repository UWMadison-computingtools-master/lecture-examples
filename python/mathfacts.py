"""
This file has functions to generate addition facts at random,
of the form '3 + 4 = ___' and '3 + ___ = 7'.
Within a python session from the same folder that the file is in,
load the library with:
from mathfacts import *
then use the mathproblem_series function to generate n problems with:
mathproblem_series(n)
or
mathproblem_series()
for a default of n=20 problems.
"""

def mathproblem(a,b,left=False):
    """
    writes an equation for the math fact a+b=c
    in which the empty spot is on the right (c is unknown),
    or on the left if left is True (b is unknown).
    In other words, the equation is:
    a + b = ___
    or
    a + ___ = c

    Examples:

    >>> mathproblem(1,4)
    '1 + 4 = __'
    >>> mathproblem(1,4,True)
    '1 + __ = 5'
    """
    c = a+b
    s = str(a) + " + "
    if left:
        s += "__ = " + str(c)
    else:
        s += str(b) + " = __"
    return s

import random

def mathproblem_series(n = 20):
    """
    print a series of n math problems, randomly generated
    with integers in 1-10.

    Example:

    >>> random.seed(4321) # for reproducibility when testing
    >>> mathproblem_series(n=4)
    1.  5 + __ = 6
    2.  2 + __ = 5
    3.  2 + 1 = __
    4.  10 + __ = 11
    """
    s = ''
    for i in range(0,n):
        a = random.randrange(1,11)
        # from 1: to avoid easy problems 0 + b = __ 
        # to 10: to include 10 + b = __
        b = random.randrange(1,11)
        left = bool(random.randrange(0,2))
        if i>0:
            s += "\n"
        s += str(i+1) + ".  " + mathproblem(a,b,left)
    print(s)
    return None
