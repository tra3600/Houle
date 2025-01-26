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


def integrale_precise(liste_niveaux):
    """
    Calcule l'intégrale approchée de η sur une période de 20 minutes en utilisant la méthode des trapèzes.
    
    Arguments :
    liste_niveaux -- Liste non vide de flottants représentant les niveaux de la mer
    
    Retourne :
    L'intégrale approchée des niveaux de la mer
    """
    n = len(liste_niveaux)
    integrale = 0.0
    
    for i in range(1, n):
        integrale += (liste_niveaux[i] + liste_niveaux[i - 1]) / 2
    
    return integrale

def moyenne_precise(liste_niveaux):
    """
    Calcule la moyenne précise de η sur une période de 20 minutes.
    
    Arguments :
    liste_niveaux -- Liste non vide de flottants représentant les niveaux de la mer
    
    Retourne :
    La moyenne précise des niveaux de la mer
    """
    integrale = integrale_precise(liste_niveaux)
    return integrale / len(liste_niveaux)

# Exemple d'utilisation
niveaux = [1, 2, 3, 4, 5]
print(moyenne_precise(niveaux))  # Output: 3.0

def ind_premier_pzd(liste_niveaux):
    """
    Trouve l'indice du premier passage par le niveau moyen en descente (PND).
    
    Arguments :
    liste_niveaux -- Liste non vide de flottants représentant les niveaux de la mer
    
    Retourne :
    L'indice du premier PND ou -1 si aucun PND n'existe
    """
    m = moyenne(liste_niveaux)
    
    for i in range(len(liste_niveaux) - 1):
        if liste_niveaux[i] > m and liste_niveaux[i + 1] < m:
            return i
    
    return -1

# Exemple d'utilisation
niveaux = [3, 2, 1, 2, 3, 0]
print(ind_premier_pzd(niveaux))  # Output: 1