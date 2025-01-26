# Ouvrir le fichier donnees.txt en mode lecture
with open('donnees.txt', 'r') as fichier:
    lignes = fichier.readlines()

# Initialiser une liste pour stocker les niveaux de la mer
liste_niveaux = []

# Parcourir les lignes en ignorant la première ligne
for ligne in lignes[1:]:
    # Convertir la ligne en flottant et l'ajouter à la liste
    niveau = float(ligne.strip())
    liste_niveaux.append(niveau)

# Afficher la liste des niveaux
print(liste_niveaux)