def calcul(mot, dic):
    """calcule la valeur d'un mot

    Args:
        mot (str): mot à calculer
    
    Returns:
        res (int):valeur du mot
    """
    res = 0
    for lettre in mot:
        if lettre in dic:
            res += dic[lettre]
    return res

def max_mot(dic_valeurs, liste):
    """détermine le mot de valeur maximum d'une liste (imprime ce mot)

    Args:
        dic_valeurs (dict): clé : lettres 
        liste (list): listes de mot
    Returns:
        valeur (int): valeur maximum 
    """
    mot = liste[0]
    valeur = calcul(mot, dic_valeurs)
    for m in liste[1:]:
        v = calcul(m, dic_valeurs)
        if v>valeur:
            mot = m
            valeur = v
    print(mot)
    return valeur

dic_valeurs = {'a':1, 'b':3}
liste=['bla', 'aba']

print(max_mot(dic_valeurs, liste))



    






