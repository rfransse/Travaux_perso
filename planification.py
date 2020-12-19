def trouve_chemin(source, destination):
    """
                Fonction qui crée un dictionnaire contenant tous les chemins possibles pour voyage d'une destination à
                une autre ainsi que leur prix

    Entrées :   source (str)        :  lettre représentant le point de départ
                destination (str)   :  lettre représentant le point d'arrivé

    Sortie  :   path (dict)         :   Clé : prix du voyage, Valeur  : chemins empruntés
    """

    def perm(prefixe, s, path, maps):
        """
        Fonction qui détermine tous les trajets possible à partir d'un maps et construit le path
        :param prefixe: (liste de tuples) contenant les trajets succéssifs
        :param s: (liste de tuples) de tous les trajets possibles
        :param path: (dict) Clé     : (float) prix des trajets
                            Valeur  : (list) liste de listes de trajets
        :param maps: (dict) Clé     : (tuple) trajets
                            Valeur  : (float) prix du trajet
        :return: None
        """

        if prefixe and prefixe[-1][1] == 'E':
            prix = calcul_prix(prefixe, maps)
            liste_prefixe = []
            for tup in prefixe:
                if tup[0] not in liste_prefixe:
                    liste_prefixe.append(tup[0])
                if tup[1] not in liste_prefixe:
                    liste_prefixe.append(tup[1])

            if prix in path:
                path[prix].append(liste_prefixe)
            else:
                path[prix] = []
                path[prix].append(liste_prefixe)

        else:
            for i in range(len(s)):
                if (not prefixe and s[i][0] == 'A') or (prefixe and s[i][0] == prefixe[-1][1]):
                    if s[i][1] not in [elem[0] for elem in prefixe]:
                        perm(prefixe + [s[i]], s[:i] + s[i + 1:], path, maps)

    def calcul_prix(prefixe, maps):
        """
        Fonction qui calcule le prix d'un trajet complet d'une source à une destination
        :param prefixe: (list) liste de tuples contenant les trajets
        :param maps: (dict) Clé     : (tuple) trajets
                            Valeur  : (float) prix du trajet
        :return: prix (float)       : prix d'un trajet complet
        """

        prix = 0

        for trajet in prefixe:
            prix += maps[trajet]

        return prix

    maps = {('A', 'B'): 11.50, ('A', 'C'): 11, ('A', 'D'): 12.50, ('B', 'C'): 11.99, ('B', 'E'): 11.50,
            ('C', 'A'): 12.40,
            ('C', 'D'): 17, ('D', 'E'): 10.50, ('D', 'A'): 11, ('E', 'B'): 10}

    path = {}

    perm([], list(maps.keys()), path, maps)


    return path


print(trouve_chemin('A', 'E'))
