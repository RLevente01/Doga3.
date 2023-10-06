"""
szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1

folytatja = True
while folytatja:
    print("Vidd ki a szemetet!")
    valasz = input ("Mondjam még egyszer? (i/n)")
    if valasz == "n":
        folytatja = False
print(">> Program vége! <<")

szam = int(input("Adj meg egy számot 5 és 10 között: "))
while not 5 <= szam <= 10:
    szam = int(input("Helytelen érték! Adj meg egy számot 5 és 10 között! "))
    print(" Rendben!")


jelszo = "alma123"
beker = input ("Kérem a jelszót: ")
while jelszo != beker:
    beker = input("Kérem a jelszót")
print("Vége a programnak")
"""  