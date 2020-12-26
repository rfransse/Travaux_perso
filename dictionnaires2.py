def motsLettresEnPosition(liste, lettre, position):
    """Returns une liste des mots contenanu une lettre à une certaine position
    """
    res = []
    dico = dicoLettreParPosition(liste)
    if (lettre, position) in dico:
        res =  dicoLettreParPosition(liste)[(lettre, position)]
    return res

def dicoLettreParPosition(liste):
    """crée un dictionnaire 

    Args:
        liste (lst): liste de mots
        
    Returns:
        dico (dict): clé: tuple (lettre, position)
                     valeurs: liste de mots
    """
    dico={}
    for mot in liste:
        for i, lettre in enumerate(mot):
            cle = lettre, i+1
            if cle in dico:
                
                dico[cle].append(mot)
            else:
                dico[cle]=[mot]
    return dico

maListe=['voici', 'une', 'liste', 'ici']
print(motsLettresEnPosition(maListe, "i", 3))
