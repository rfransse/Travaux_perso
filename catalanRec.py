def catalanRec(L, n):
    """construit la liste des n premiers nombres de catalan

    Args:
        L (list): liste des nombres de catalan
        n (int): nombre d'éléments dans la liste

    Returns:
        c (int): n_ème nombre de catalan
    """
    if n == 1:
        c = 1
        L.append(c)
    else:
        c = 2*(2*n-3)/n*catalanRec(L, n-1)
        L.append(c)
    return c

L  = []
print(catalanRec(L, 5), L)