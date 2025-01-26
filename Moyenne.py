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


def moyenne(liste_niveaux):
    """
    Calcule la moyenne des éléments d'une liste non vide.
    
    Arguments :
    liste_niveaux -- Liste non vide de flottants représentant les niveaux de la mer
    
    Retourne :
    La moyenne des éléments de la liste
    """
    return sum(liste_niveaux) / len(liste_niveaux)

# Exemple d'utilisation
niveaux = [1, 2, 3, 4, 5]
print(moyenne(niveaux))  # Output: 3.0