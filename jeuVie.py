"""Programme du Jeu de la Vie
"""

def Init(m):
    """crée un ensemble de vivants

    Args:
        m (int): dimension de la matrice

    Returns:
        res (set of tuples): ensemble des positions des vivants dans la matrice de dimension m
    """
    res = set()
    a= None

    while a != "0,0":
        a= input(f"Position i,j d'un vivant dans la matrice {m}x{m}  (0,0 pour terminer) : ")
        if a != "0,0":
            b = a.split(',')
            c = int(b[0]), int(b[1])
        res.add(c)

    return res

def Execute(ensembleDEtats, m, nbreDEtapes):
    """exécute plusieurs étapes du jeu de la vie et affiche le résultat final (ensemble des vivants)

    Args:
        ensembleDEtats (set): ensemble de couples, correspondant aux vivants
        m (int): taille de la matrice
        nbreDEtapes (int): nombre d'étapes du jeu à effectuer
    """

    def nbreVivant(case, ensembleDEtats):
        """détermine le nombre de voisins vivants d'une case

        Args:
            case (tup): coordonnées d'une case de la matrice
            ensembleDEtats (set): ensemble des vivants
        
        Returns:
            res (int): nombres de vosins vivants
        """
        #res = 0
        #for u in (-1, 0, 1):
            #for v in (-1, 0, 1):
                #if (u, v) != (0, 0) and (case[0]+u, case[1]+v) in ensembleDEtats: 
                        #res += 1

        return len ({(case[0]+i,case[1]+j) for i in (-1,0,1) for j in (-1,0,1) if (i,j) !=(0,0) and (case[0]+i, case[1]+j) in ensembleDEtats})

        #return res

    for etape in range(nbreDEtapes):
        for case in [(i,j) for i in range(1, m+1) for j in range(1, m+1)]:
            if case in ensembleDEtats:
                if nbreVivant(case, ensembleDEtats) not in {2, 3}:
                    ensembleDEtats.remove(case)
            elif nbreVivant(case, ensembleDEtats) == 3:
                ensembleDEtats.add(case)

    # impression des résultats (matrice et ensemble des vivants)
    for i in range(1, m+1):
        for j in range(1, m+1):
            if (i,j) in ensembleDEtats:
                print("V", end=" ")


            else:
                print("M", end=" ")
        print()
    print('Vivants :', ensembleDEtats)

# corps principal

m = 3
nbreDEtapes = 2
Execute(Init(m), m, 2)

