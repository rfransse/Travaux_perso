def amis(bdd, nom, d):
    """détermine les amis situés à une distance d'au plus d

    Args:
        bdd (dict): keys (str) :    username
                    values (list) : list of friends
        nom (str): username
        d (int): distance_max avec le username

    Returns:
        res (list): list of friends
    """     
    def f(bdd, nom, k, d_max, res):
        
        if k == d_max-1: # cas de base je prends les amis du noeud de distance dmax-1
                if nom in bdd:
                    res = res + bdd[nom]
                
        else:
            if nom in bdd: # si la personne a des amis
                for ami in bdd[nom]: # pour chaque ami du nom             
                        res = [ami] + f(bdd, ami, k+1, d_max, res) # le résultat est l'ami et leurs ami
        
        return res
    
    res = set(f(bdd, nom, 0, d, []))
    res.discard(nom)
    return res


bdd = {'Lambert': ['Jaco', 'Adrien'], 'Jean': ['Pierre', 'Jacques'], 'Pierre' : ['Jean', 'Patrick'], 'Patrick': ['Lambert', 'Jules']}
print(amis(bdd, 'Jean',4))