def merge(l1, l2):
    """fusionne 2 listes triées

    Args:
        l1 (list): liste1
        l2 (list): liste2
        
    returns: res (list): liste fusionnée et triée
    """
    if l2 == []:
        res = l1
    elif l1 == []:
        res = l2
    else:
        pos = 0
        ajout = l2[pos]
        while pos<len(l1) and ajout >= l1[pos]:
            pos +=1
        res = merge(l1[:pos]+[ajout]+l1[pos:], l2[1:])
    return res

print(merge([1,2,3,4,5,13, 57,60, 70], [3,6,9,11,12, 15,50, 72]))