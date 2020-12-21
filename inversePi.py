def estimation(e=0.01, maxloops=50):
    """estime l'investre de pi
    """
    f = lambda x: x*f(x-1) if x>1 else 1
    cste = (2*2**0.5)/9801
    g = lambda k : cste * f(4*k) * (1103 + 26390*k) / f(k)**4 / 396**(4*k)

    k = 1
    dif = e + 1
    s = g(0)

    while k < maxloops and dif > e:
        prec = s
        s = s + g(k)
        dif = abs(prec - s)
        k +=1

    return  s

print(estimation())

