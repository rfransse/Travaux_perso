

def amis(bdd, nom, k, d):
    """détermine les éméments d'un arbre"""

    print(nom)

    if nom in bdd:
        for ami in bdd[nom]:
            amis(bdd, ami, k, d)


def amis2(bdd, nom, k, d):
    """détermine les éléments d'un niveau max à 2"""
    if k>0 :
        print(nom)

    if nom in bdd and k<d:
        for ami in bdd[nom]:
            amis2(bdd, ami, k+1, d)

def amis3(bdd, nom, k, d, s):
    
    s.append(nom)

    if nom in bdd and k<d:
        for ami in bdd[nom]:
            if ami not in s:
                amis3(bdd, ami, k+1, d, s)
    
    return s
    

bdd = {'Lambert': ['Jaco', 'Adrien'], 'Jean': ['Pierre', 'Jean', 'Jacques'], 'Pierre' : ['Phil', 'Patrick'], 'Patrick': ['Lambert', 'Jules']}
#amis2(bdd, 'Jean',0, 3)

print(amis3(bdd, 'Jean', 0, 3, []))
