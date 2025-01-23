#Même programme que #3, mais avec une boucle
print("Donner un nombre")
CALCUL = int(input())
RÉPONSE = 1
for i in range(CALCUL-1):
    RÉPONSE = RÉPONSE*(i+2)
    print(RÉPONSE)
print("la factorielle est",RÉPONSE)