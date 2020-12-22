def catalanIter(L, n):
    """construit la liste des n premiers nombres de catalan

    Args:
        L (list): liste des nombres de catalan
        n (int): nombre d'éléments dans la liste

    Returns:
        c (int): n_ème nombre de catalan
    """
    c = 1
    L.append(c)
    for k in range(2,n+1):
        c *= 2*(2*k-3)/k
        L.append(c)
    return c
L=[]
print(catalanIter(L, 3), L)