
def polybe(message, clef):
    i, j, k, ensemble, message, mot = 0, 0, 0, set(), message.replace('w','v').replace(' ',''), clef + "abcdefghijklmnopqrstuvxyz" 
    while len(ensemble) < 25:
        if mot[k] not in ensemble:
            message, ensemble, i, j = message.replace(mot[k], str(i)+str(j)), ensemble|{mot[k]}, i+(j+1)//5, (j+1)%5
        k += 1         
    return message
print(polybe('fuyons nous cette nuit', 'chiffrement'))
    
            
        
                    
                
        