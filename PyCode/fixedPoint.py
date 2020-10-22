def fpi(g, x0, k):
    '''Attempts to used Fixed Point Iteration to determine x such that g(x) = x given
       an initial guess x0.

    Parameters
    ----------
    g : function
        Function g(x) used to find fixed point x

    x0 : integer of float
        Initial guess for fixed point used to begin iteration.

    k : integer
        Integer greater than zero that represents the number of times we should
        iterate.

    Returns
    -------
    x : Fixed point estimate
        Approximation of fixed point given by the final iteration of the algorithm.
    '''

    i = 0
    x = g(x0)


    while i < k:
        x = g(x)
        i += 1
    return x