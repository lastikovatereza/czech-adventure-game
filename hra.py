from lokace import Lokace


class Hra:
    hrad = Lokace("Hrad",
                  "Stojíš před okovanou branou gotického hradu, která je zřejmě jediným vchodem do pevnosti. Klíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
    les1 = Lokace("Les",
                  "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    les2 = Lokace("Lesní rozcestí", "Nacházíš se na lesním rozcestí.")
    les3 = Lokace("Les",
                  "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    rybnik = Lokace("Rybník",
                    "Došel jsi ke břehu malého rybníka. Hladina je v bezvětří jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
    les4 = Lokace("Les",
                  "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    dum = Lokace("Dům",
                 "Stojíš před svým rodným domem, citíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dvěří.")

    # Uložení aktuální lokace
    aktualni_lokace = dum

    # Zde dokonči úlohu svým kódem...
    def __init__(self):
        self.hrad.vychod = self.les1
        self.les1.zapad = self.hrad
        self.les1.vychod = self.les2
        self.les2.zapad = self.les1
        self.les2.vychod = self.les3
        self.les3.zapad = self.les2
        self.les3.vychod = self.rybnik
        self.rybnik.zapad = self.les3

        self.les1.jih = self.les4
        self.les4.sever = self.les1
        self.les4.vychod = self.dum
        self.dum.zapad = self.les4

        self.aktualni_lokace = self.dum

    def zpracuj_prikaz(self, prikaz):
        prikaz = prikaz.strip().lower()

        if prikaz == "konec":
            return False

        if prikaz.startswith("jdi na "):
            smer = prikaz[7:]

            nova_lokace = None
            if smer == "sever":
                nova_lokace = self.aktualni_lokace.sever
            elif smer == "jih":
                nova_lokace = self.aktualni_lokace.jih
            elif smer == "východ":
                nova_lokace = self.aktualni_lokace.vychod
            elif smer == "západ":
                nova_lokace = self.aktualni_lokace.zapad
            else:
                print("Můj vstupní slovník neobsahuje tento příkaz.")
                return True

            if nova_lokace:
                self.aktualni_lokace = nova_lokace
                self.vypis_lokaci()
            else:
                print("Tímto směrem nelze jít.")
        else:
            print("Můj vstupní slovník neobsahuje tento příkaz.")

        return True

    def vypis_lokaci(self):
        print()
        print(self.aktualni_lokace.nazev)
        print(self.aktualni_lokace.popis)
        dostupne = self.aktualni_lokace.dostupne_smer()
        print("\nMůžeš jít na " + " ".join(dostupne))