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
    # Check if there is a zero within the interval taking advantage of the intermediate value theorem
    if f(a)*f(b) >= 0:
        print('Bisection Method Failed')
        return None
    
    n = 1 # Used to count number of iterations

    while (b-a)/2 > tol:
        c = (a+b)/2
        n += 1
        if f(c) == 0:
            print('Value found!')
            return c
        if f(a)*f(c) < 0:
            a = a
            b = c
        else:
            a = c
            b = b
    return (a + b)/2