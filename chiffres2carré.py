def doubleplayfair(cle1, cle2, msg):
    """fournit un message codé à partir de 2 clés

    Args:
        cle1 (str): mot de 5 lettres
        cle2 (str): idem
        msg (str): message à coder
    Returns:
       res(str): message traduit
    """
    matrice1, matrice2 = matrice(cle1, cle2)
    msg = msg.replace(' ','')
    res = ''
    if len(msg) % 2:
        msg = msg + "X"
    for i in range(0,len(msg),2):
        # p1 et p2 sont les positions des deux lettres dans leur matrice
        p1, p2 = position(matrice1, msg[i]), position(matrice2, msg[i+1])
        
        res += matrice1[p1[0]][p2[1]] + matrice2[p2[0]][p1[1]]
    return res  

def matrice(cle1, cle2):
    """returns tuple de 2 matrices à partir des deux clés"""
    cles = cle1.replace('J','I'), cle2.replace('J', 'I')
    matrices = [[None for _ in range(5)] for _ in range(5)], [[None for _ in range(5)] for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    for i in range(2):
        matrices[i][0] = list(cles[i])
        alpha = [lettre for lettre in alphabet if lettre not in matrices[i][0]]
        positionDansAlphabet = 0
        for j in range(1,5):
            for k in range(5):
                matrices[i][j][k] = alpha[positionDansAlphabet]
                positionDansAlphabet += 1
    return matrices

def position(matrice, lettre):
    """Renvoie le couple de position dans une matrice"""
    lettre = lettre.replace('J', 'I')
    j = 0
    while lettre not in matrice[j]:
        j +=1
    return (j, matrice[j].index(lettre))


# ***************** corps du PRG ****************************  

cle1, cle2, msg = 'JAUNE', 'IDOTA', 'JAMAIS DE LA VIE'

print('message à (dé)crypter : ', msg)
print()
for m in matrice(cle1, cle2):
    for i in range(5):
        for j in range(5):
            print(m[i][j], end=' ')
        print()
    print()

print(doubleplayfair(cle1, cle2, msg))