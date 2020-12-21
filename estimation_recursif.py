def estimation(k=0, e=0.01, maxloops=50):
    """estime l'investre de pi
    """
    f = lambda x: x*f(x-1) if x>1 else 1
    cste = (2*2**0.5)/9801
    g = lambda k : cste * f(4*k) * (1103 + 26390*k) / f(k)**4 / 396**(4*k)

    if k >= maxloops or dif < e:
    
    else:
        res = f()
        
    return  s

print(estimation())
