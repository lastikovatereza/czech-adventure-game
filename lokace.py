class Lokace:
    # Lokace na severu
    sever = None

    # Lokace na jihu
    jih = None

    def __init__(self, nazev, popis):
        self.nazev = nazev
        self.popis = popis
        self.sever = None
        self.jih = None
        self.vychod = None
        self.zapad = None

    def dostupne_smery(self):
        smery = []
        if self.sever: smery.append("sever")
        if self.jih: smery.append("jih")
        if self.vychod: smery.append("východ")
        if self.zapad: smery.append("západ")

        return smery
