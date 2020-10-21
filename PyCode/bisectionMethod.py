def bisect(f,a,b,tol):

    if f(a)*f(b) >= 0:
        print('Bisection Method Failed')
        return None
    
    while (b-a)/2 > tol:
        c = (a+b)/2
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