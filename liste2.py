def reshape(lst, shape):
    """construit une liste selon une fonction de numpy

    Args:
        lst (list): liste d'entiers
        shape (tuple):  composante1: nombre de liste à construire
                        composante2: nombre d'entiers par liste ou -1
                        
    Return: res: None si shape incompatible
                 list de lst créée
    """
    if compatible(lst, shape):
        L = [lst[i][j] for i in range(len(lst)) for j in range(len(lst[i]))]
        if shape[1] == -1:
            a, b = shape[0], len(lst)*len(lst[0])//shape[0]
        else:
            a, b = shape[0], shape[1]
        res = []
        for i in range(a):
            res += [ L[i*b:(i+1)*b] ]
        return res

def compatible(lst, shape):
    """teste la compatibilité des données"""  
    
    res = True
    # vérification de lst (à faire)
        # vérifier que j'ai une liste de liste d'entiers      
    # vérification de shape
    
    long = len(lst) * len(lst[0])
    if type(shape[0]) != int or type(shape[1]) != int:
        res = False
    elif shape[0] <= 0:
        res = False
    elif shape[1] == -1 and long%shape[0] != 0:
        res = False
    elif shape[1] != -1 and shape[1] * shape[0] != long:
        res = False
    
    return res
print(reshape(    [[1, 2], [3, 4], [5, 6]], (2,-1)   ))