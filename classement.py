def rangement(filename):
    """classe les éléments d'un fichier dans un dictionnaire

    Args:
        filename (str): nom du fichier texte
         
    Returns:
        dict : dic (dict): clé: catégorie, valeur: dict: clé: name_application, valeur : (nbr_achats, nbr_stars)
    """
    dico = {}
    with open(filename, encoding="utf-8") as file:
        lst = file.readlines()
    for elem in lst:
        record = elem.strip().split(sep=":")
        name_application, category, stars = record[1:]
        if category in dico:
            if name_application in dico[category]:
                dico[category][name_application][0] +=1
                dico[category][name_application][1] += int(stars)
            else:
                dico[category][name_application]=[1, int(stars)]
        else:
            dico[category] = {name_application : [1, int(stars)]}
    return dico
def triDecroissant(lst):
    """trie une liste par ordre décroissant

    Args:
        lst (list): liste de couples (name_application, (nbr, star)) à trier selon un critère65/35
    """ 
    f = lambda x: 0.65*x[0] + 0.35*(x[1]/x[0])
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if f(lst[j][1]) > f(lst[i][1]):
                lst[i], lst[j] = lst[j], lst[i]
        
### corps principal ###
filename = "classe.txt"
dico = rangement(filename) 

print(dico)

for application in dico: 
    lst = list(zip(dico[application].keys(), dico[application].values()))
    #print(lst)
    triDecroissant(lst)
    print()
    print('top 10', application + ':')
    for i, name_application in zip(range(1, 11), [name[0] for name in lst]):
        print(i, '-', name_application)
    
        
        
        
        