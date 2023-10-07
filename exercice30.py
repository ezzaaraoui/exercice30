nombre=int(input("taper un entier n : "))

while nombre<0 :
    nombre=int(input("taper un entier (positif ou null): "))
Ui=6
if nombre==0 :
    print(Ui)
else:
    for i in range(1,nombre+1):
        Un=4*Ui +10
        Ui=Un
    print("le resultat est : ",Un)