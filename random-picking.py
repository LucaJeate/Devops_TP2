from math import comb

def proba_tirage_uniforme(k, nb_noires, nb_blanches, nb_rouges):
    total_boules = nb_noires + nb_blanches + nb_rouges

    # Vérifier si le nombre de boules tirées est valide
    if k > total_boules:
        raise ValueError("Le nombre de boules tirées ne peut pas être supérieur au nombre total de boules.")

    # Calcul des combinaisons pour obtenir une boule de chaque couleur
    comb_noires = comb(nb_noires, 1)
    comb_blanches = comb(nb_blanches, 1)
    comb_rouges = comb(nb_rouges, 1)

    # Calcul du nombre total de façons d'obtenir k boules parmi toutes les boules
    comb_total = comb(total_boules, k)

    # Calcul de la probabilité
    proba = (comb_noires * comb_blanches * comb_rouges) / comb_total

    return proba

# Exemple d'utilisation
k = 3
nb_noires = 5
nb_blanches = 4
nb_rouges = 3

probabilite = proba_tirage_uniforme(k, nb_noires, nb_blanches, nb_rouges)
print(f"La probabilité d'obtenir une boule de chaque couleur en tirant {k} boules est : {probabilite:.4f}")