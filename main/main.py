from bean.Citadine import *
from bean.Familiale import *
from bean.Utilitaire import *
from Vehicule import *

citadine = Citadine("rouge", 5, 250)
citadine1 = Citadine("marron", 6, 450)
citadine2 = Citadine("blanche", 3, 750)
citadine3 = Citadine("violette", 5, 490)

utilitaire = Utilitaire("gerte", 5, 950)
utilitaire1 = Utilitaire("grise", 3, 1200)

familiale = Familiale("bleue", 5, 9)
familiale1 = Familiale("blanche", 7, 12)
familiale2 = Familiale("benzema", 9, 15)

citadine.rouler()
utilitaire.rouler()
familiale.rouler()

# Boucle liste pour tout afficher :
for i in Vehicule.liste_vehicules:
    print(i.__str__())
# Boucle liste pour tout afficher.

# Connaitre le nombre de voitures total dans la liste tout :
print(f"Le nombre total de voiture est de : ", len(Vehicule.liste_vehicules))
# Connaitre le nombre de voitures total dans la liste tout.


# Boucle liste pour afficher et compter les Citadines :
stock = 0
for i in Vehicule.liste_vehicules:
    if type(i) == Citadine:
        stock += 1
        print(i.__str__())
print(f"Le nombre total de voitures citadines est de : {stock}")
# Boucle liste pour afficher et compter les Citadines.


# Boucle liste pour afficher et compter les Utilitaires :
stock = 0
for i in Vehicule.liste_vehicules:
    if type(i) == Utilitaire:
        stock += 1
        print(i.__str__())
print(f"Le nombre total de voitures utilitaires est de : {stock}")
# Boucle liste pour afficher les Utilitaires.


# Boucle liste pour afficher et compter les Familiales :
stock = 0
for i in Vehicule.liste_vehicules:
    if type(i) == Familiale:
        stock += 1
        print(i.__str__())
print(f"Le nombre total de voitures familiales est de : {stock}")
# Boucle liste pour afficher les Familiales.
