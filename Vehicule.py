from abc import ABC


class Vehicule(ABC):
    liste_vehicules = []

    def __init__(self, couleur, nbrPorte):
        self._couleur = couleur
        self._nbrPorte = nbrPorte
        self.liste_vehicules.append(self)

    @property
    def couleur(self):
        return self._couleur

    @property
    def nbrPorte(self):
        return self._nbrPorte

    @couleur.setter
    def couleur(self, c):
        self._couleur = c

    @nbrPorte.setter
    def nbrPorte(self, n):
        self._nbrPorte = n

    def rouler(self):
        print("La voiture roule")