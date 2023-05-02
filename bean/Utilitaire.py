from Vehicule import Vehicule


class Utilitaire(Vehicule):

    def __init__(self, couleur, nbrPorte, poids_total):
        super().__init__(couleur, nbrPorte)
        self.poids_total = poids_total

    @property
    def couleur(self):
        return super().couleur

    @property
    def nbrPorte(self):
        return super().nbrPorte

    def rouler(self):
        super().rouler()

    def __str__(self):
        return f"Utilitaire : la couleur est : {self.couleur}, le nombre de porte est de {self.nbrPorte} et le poids total peut aller jusqu'à {self.poids_total} kgs."

