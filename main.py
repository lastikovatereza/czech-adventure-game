from Cviceni.hra import Hra

hra = Hra()
prikaz = ""

# Zde dokonči úlohu svým kódem...

hra.vypis_lokaci()

while True:
    prikaz = input("\nZadej příkaz: ")
    if not hra.zpracuj_prikaz(prikaz):
        break