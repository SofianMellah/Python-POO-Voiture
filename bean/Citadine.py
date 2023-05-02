from Vehicule import Vehicule


class Citadine(Vehicule):

    def __init__(self, couleur, nbrPorte, autonomie):
        super().__init__(couleur, nbrPorte)
        self.autonomie = autonomie

    def rouler(self):
        return super().rouler()
    @property
    def couleur(self):
        return super().couleur

    @property
    def nbrPorte(self):
        return super().nbrPorte

    def __str__(self):
        return f"Citadine : la couleur est : {self.couleur}, le nombre de porte est de {self.nbrPorte} et l'autonomie est de {self.autonomie}kms."
