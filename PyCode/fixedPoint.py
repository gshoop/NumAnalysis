def fpi(g, x0, k):
    '''


    '''

    i = 0
    x = g(x0)
    

    while i < k:
        x = g(x)
        i += 1
    return x