def calcule_carres(n) :
    
    Nombre_carres = 0
    for i in range(1, n+1):
        Nombre_carres = Nombre_carres + i**2 
    print("le nombre des carres est : " + str(Nombre_carres))

n = int(input("Donner la dimension de votre carré (uniquement un entier) : "))
calcule_carres(n)