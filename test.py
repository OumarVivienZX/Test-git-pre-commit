# fontion manger attiéké


class Mangerattiéké:

    def __init__(self, non, mange, quantite):
        self.non = non
        self.mange = mange
        self.quantite = quantite

    def manger(self):
        print(f"{self.non} mange {self.quantite} d'attiéké")


personne1 = Mangerattiéké("Adama", "attiéké", "500g")
personne1.manger()
