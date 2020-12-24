def rule101(maxIter):
    """applique un certain nombre de fois la règle 101 à une matrice 50x50

    Args:
        maxIter (int): nombre max d'itérations à faire

    Returns:
        M (list): la matrice finale
    """

    def modif(M):
        """applique la règle 101 à la matrice M dans une matrice M_T:

        Args:
            M (list): matrice

        Returns:
            M_T (list): Matrice qui comprend les modifications
        """
        
        M_T = [[0 for _ in range(50)] for  _ in range(50)]

        for i in range(50):
            for j in range(1, 49):

                tup = M[i][j-1], M[i][j], M[i][j+1]

                if tup==(1,1,1): 
                    M_T[i][j] = 0

                elif tup==(1,1,0): 
                    M_T[i][j] = 1

                elif tup==(1,0,1): 
                    M_T[i][j] = 1

                elif tup==(1,0,0):
                    M_T[i][j] = 0

                elif tup==(0,1,1):
                    M_T[i][j] = 0

                elif tup==(0,1,0):
                    M_T[i][j] = 1

                elif tup==(0,0,1):
                    M_T[i][j] = 0

                elif tup==(0,0,0):
                    M_T[i][j] = 1
               
        return M_T

    def imprimer(M):
        """imprime la matrice M
        """
        for i in range(50):
            for j in range(50):
                print(M[i][j], end=" ")
            print()

    # corps principal de rule101

    M=[[0 for _ in range(50)] for _ in range(50)]
    t=0
    flag=True

    while t<maxIter and flag:
        M_T=modif(M)
        flag= M != M_T
        t=t+1
        M=M_T

    imprimer(M)
    return M

rule101(10)
