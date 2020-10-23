from numpy import sign
from numpy import log2

def bisect(f,a,b,tol):
    '''Approximates zeros of f(x) between interval [a,b] using bisection method.
    
    Parameters
    ----------
    f : function
        The function we are looking for zeros of
    
    a,b : int or floats
        The interval to be searched. If f(a)*f(b) > 0 the function returns nothing
        since there are no zeros within the interval [a,b]

    tol : decimal value
        The decimal place to which we will approximate the solution.

    Returns
    -------
    c_n : Midpoint of last iteration
        This is the approximation of the solution to f(x)=0 in the interval [a,b]

    Test Case
    ---------
    '''
    #from numpy import sign
    # Check if there is a zero within the interval taking advantage of the intermediate value theorem
    if f(a)*f(b) >= 0:
        print('Bisection Method Failed')
        return None
    
    i = 0 # Used to count number of iterations
    n = log2((b-a)/(2*tol))
    print('\nEstimated number of steps needed n = {}'.format(n))
    # Formating for table
    # Table will show iteration number i, along with values of a, b, and c at i
    # and the signs of a, b, and c represented with -1 or 1.
    print('\n i |   ai   |f(ai)|   ci   |f(ci)|   bi   |f(bi)|')
    
    # Loop runs while half the distance between our interval is greater than our tolerance
    # returns our approximation when we are below the tolerance
    while (b-a)/2 > tol:
        c = (a+b)/2                 # halfway point in interval
        print('%2d |%8.6f|%5d|%8.6f|%5d|%8.6f|%5d|' %(i,a,sign(f(a)),c,sign(f(c)),b,sign(f(b))))
        i += 1                      # incrementing count for iterations
        if f(c) == 0:               # we've found a zero if f(c) == 0
            print('Value found!')
            return c
        if f(a)*f(c) < 0:           # If true IVT says zero is between [a,c]
            a = a
            b = c                   
        else:                       # else zero must be between [c,b]
            a = c
            b = b
    
    c_n = (a+b)/2
    print('\nNumber of iterations: {}'.format(i))
    return c_n