import  random
import  math

# Írj eljárást, mely a paraméterében kap két egész számot
# ezen két egész szám közötti
# páros számok összegét számolja ki az eljárást

def elsoFeladat(szamEgy,szamKetto):
    index = szamEgy
    osszeg = 0
    while index <= szamKetto:
        if index % 2 == 0:
            print(index)
            osszeg += index
        index+=1
    return osszeg

    # parosSzam = 0
    # osszeguk = 0
    # while szamEgy < szamKetto:
    #    if szamEgy % 2 == 0:
    #        parosSzam += szamEgy
    #    szamEgy+=1
    #print(parosSzam)



# írj függvényt amely generál 10 db véletlen számot
# -10 és 10 között
# Számold meg hány negatív szűm van közötte
# a visszatérési érték negativ számok száma

def negativ():
    negativakSzama = 0
    index = 0
    while index < 10:
        randomSzam = math.floor(random.random() * (10+10)-10)
        if randomSzam < 0:
            negativakSzama += 1
        index += 1
    return  negativakSzama

def negativKetto():
    negativakSzama = 0
    index = 0
    for i in range(0,20,1):
        randomSzam = math.floor(random.random() * (10 + 10) - 10)
        if randomSzam < 0:
            negativakSzama += 1
    return negativakSzama

def parosKetto(szamEgy,szamKetto):
    osszeg = 0
    for index in range(szamEgy,szamKetto,1):
        if index % 2 == 0:
            print(index)
            osszeg += index
    return osszeg


# Írj függvényt amely generál 10 db véletlen számot 12 és 33 között
# visszatér ezek összegével

def veletlenSzamokTizenkettoHarmincharom():
    osszeg = 0
    for i in range(0,10,1):
        randomSzam = math.floor(random.random()*(34-12)+12)
        osszeg += randomSzam
    return  osszeg

# Írj függvényt amely generál 8 db véletlen számot
# [20,50) intervalumban és visszatér ezek közül a legnagyobb számmal

def legnagyobbSzam():
    nagyobbSzam = 0
    for i in range(0,8,1):
        randomSzam = math.floor(random.random()*(50-20)+20)
        if nagyobbSzam < randomSzam:
            nagyobbSzam = randomSzam
    return  nagyobbSzam

# Kérjünk be 3 db egész számokat a felhasználótól
# mekkor a számok átlaga?

def bekeresHarom():
    osszegzes = 0
    atlag = 0
    for i in range(0,3,1):
        szamBekeres:int = int(input("Szeretnek kerni egy számot: "))
        osszegzes += szamBekeres
        atlag = round((osszegzes / 3))
    return atlag


# Kérjünk be egész számokat a felhasználótól amíg 0-at nem add
# Írjuk ki a számok átlagát

def bekeresAtlag():
    db = 0
    osszegzes = 0
    szamBekeres:int = int(input("Szeretnek kerni egész számokat, 0-ig: "))
    while not szamBekeres == 0:
        db += 1
        osszegzes += szamBekeres
        szamBekeres: int = int(input("Szeretnek kerni egész számokat, 0-ig: "))
    return round(osszegzes / db)
