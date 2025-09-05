from Cviceni.hra import Hra

hra = Hra()
prikaz = ""

hra.vypis_lokaci()

while True:
    prikaz = input("\nZadej příkaz: ")
    if not hra.zpracuj_prikaz(prikaz):

        break
