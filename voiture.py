def tirette(bande_droite, bande_gauche):
    """affiche l'ordre de passage des voitures

    Args:
        bande_droite (list): liste de couleurs
        bande_gauche (list): liste de couleurs
    """

    def tirer(bande_select, bande_autre, k):
        
        if bande_select:
            print(k, bande_select[0])
            tirer(bande_autre, bande_select[1:], k+1)
        elif bande_autre:
            print(k, bande_autre[0])
            tirer(bande_autre[1:], bande_select, k+1)
        else:
            return None

    # corps de la fonction tirette
    return tirer(bande_droite, bande_gauche, 1)

tirette(['rose', 'verte', 'bleue', 'orange'], ['rouge', 'noire'])

