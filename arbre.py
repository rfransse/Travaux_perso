
def isTree(lst):

    def parcours(noeud, ensemble, res):
        if noeud in ensemble:
            res = False
        else:       
            ensemble.add(noeud)                       
            for fils in noeud[1]:
                parcours(fils, ensemble,res)         
        return res    
    
    return parcours(lst, set(), True)
        
        
node1 = [7,[]]
node2 = [8,[]]
node3 = [9,[]]
node4 = [5,[]]
node5 = [10,[]]
node6 = [6,[node5]]
node8 = [4,[node1, node2, node3]]
node9 = [2,[node8]]
node7 = [3,[node4, node6]]
tree1 = [1, [node9, node7]]

print(isTree(tree1))