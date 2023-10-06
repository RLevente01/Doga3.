#1.feladat: Kérjünk be 5 db egész számot és minden páros számot irjunk ki még egyszer
"""
for x in range(1,6,1):
    szam = int(input("Kérem a számot: "))
    if szam %2 == 0:
        print(f"A megadott {szam} páros") 
"""







#be kérni még 10-et és amelyik osztható 3-mal irja ki a dupláját

for x in range(1,11,1):
    s = int(input("Kérem a számot: "))
    if s %3 == 0:
        dupla = s * 2 
        print(f"A megadott {s} kétszerese: {dupla} ") 


        