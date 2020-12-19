def pivot(s):
    """Fonction qui détermine le pivot d'une liste

    Args:
        s (list): liste d'entiers

    Returns:
        piv (int) : pivot de la liste s ou None si pas de pivot
    """

    i = len(s)-1
    pivot = None

    while pivot is None and i >= 0:
        if i == len(s)-1:
            if sum(s[:i]) == 0:
                pivot = i
        else:
            if sum(s[:i]) == sum(s[i+1:]):
                pivot = i
        
        i -= 1
    
    return pivot

print(pivot([1,-1,1,-1,1,-1,1]))