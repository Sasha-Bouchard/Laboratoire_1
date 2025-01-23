#Programme qui calcule la factorielle d'un nombre
print("Donner un nombre")
CALCUL = int(input())
def calcul_factorielle(i):
    if (i>1):
        RÉPONSE = i*calcul_factorielle(i-1)
    if (i==1 or i==0):
        RÉPONSE = 1
    return(RÉPONSE)
print("la factorielle est",calcul_factorielle(CALCUL))
