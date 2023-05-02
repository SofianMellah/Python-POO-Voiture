from Vehicule import Vehicule


class Familiale(Vehicule):

    def __init__(self, couleur, nbrPorte, nombre_de_places):
        super().__init__(couleur, nbrPorte)
        self.nombre_de_places = nombre_de_places

    @property
    def couleur(self):
        return super().couleur

    @property
    def nbrPorte(self):
        return super().nbrPorte

    def rouler(self):
        super().rouler()

    def __str__(self):
        return f"Familiale : la couleur est : {self.couleur}, le nombre de porte est de {self.nbrPorte} et le nombre de place est de {self.nombre_de_places} places."
