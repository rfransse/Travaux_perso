def pivot(s, i):
    """Fonction récursive qui détermine l'indice pivot d'une séquence s

    Args:
        s (list): liste d'entiers
        i (int): indice du candidat pivot
    
    Returns:
        piv (int) : indice du pivot
    """
    if i < 0:
        piv = None 

    elif i == len(s)-1 and sum(s[:i]) == 0:
        piv = i

    elif sum(s[:i]) == sum(s[i+1:]):
        piv = i
    
    else:
        piv = pivot(s, i-1)

    return piv

s = [1,2,4]

print(pivot(s, len(s)-1))