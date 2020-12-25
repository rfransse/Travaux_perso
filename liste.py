def reception(stock, livraisons):
    """modifie un stock suite à une livraisons

    Args:
        stock (list): liste de liste composée du nom d'un produit et de son stock
        livraisons (list): liste de liste de même forme que livraisons
    """
    for [produit, quantite] in livraisons:
        i=0
        while i<len(stock) and produit != stock[i][0]:
            i+=1
        if i ==len(stock):
            stock.append([produit, quantite])
        else:
            stock[i][1]+=quantite

def commande(stock, commandes):
    """modifie un stock suite à une commande

    Args:
        stock (lst): up
        commandes (lst): up
        
    Returns:
        res(bool): True si la commande est complètement honorée, False sinon
    """
    # vérification que la commande peut être honorée
    res=True
    i=0
    while i<len(commandes) and res==True:
        j=0
        while j<len(stock) and res==True:
            if stock[j][0] == commandes[i][0] and commandes[i][1] > stock[j][1]:
                res=False
            j+=1
        if j==len(stock):
            res=False
        i+=1       
    if res:
        # modification du stock
        for [produit, quantite] in commandes:
            i=0
            while produit != stock[i][0]:
                i+=1
            stock[i][1]-=quantite
            if stock[i][1]==0:
                stock.remove(stock[i])    
    return res

stock = [['coca', 10], ['sprite', 10],['fanta', 10]]
livraisons = [['coca', 5], ['sprite', 6],['fanta', 7], ['redbull', 8]]
commandes = [['coca', 8], ['sprite', 16],['redbull', 7]]
reception(stock, livraisons)
print(stock)
print(commande(stock, commandes))
print(stock)
print(commande(stock, [['redbull', 2]]))
print(stock)