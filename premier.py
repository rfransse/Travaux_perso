def premier(A):
    """Retourne la liste des premiers inférieurs à A
    """
    L = [] 
    if A > 1:
        for B in range(2, A+1):
            reste = 1
            n = 2
            while n*2 <= B and reste:
                reste = B % n
                n +=1
            if reste:
                L.append(B)
    return L

def permutation(prefixe, lst, L, n):
    if len(prefixe)==n:
        produit = 1
        for facteur in prefixe:
            produit *= facteur
        if produit not in L:
            L.append(produit)
    else:
        for premier in lst:
            permutation(prefixe + [premier], lst, L, n)

def prodPremier(n, A):
    L=[]
    lst = premier(A)
    permutation([], lst, L, n)
    return L
    
print(prodPremier(2, 4))
    


          
          
        
        