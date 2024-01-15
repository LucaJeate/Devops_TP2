from math import comb

def proba_tirage_uniforme(k,nb_noires,nb_blanches,nb_rouges):
    total_boules=nb_noires+nb_blanches+nb_rouges

    if k > total_boules:
        raise ValueError("Le nombre de boules tirées incohérent.")

    comb_noires = comb(nb_noires,1)
    comb_blanches = comb(nb_blanches,1)
    comb_rouges = comb(nb_rouges,1)

    comb_total = comb(total_boules,k)

    proba = (comb_noires*comb_blanches*comb_rouges)/comb_total

    return proba

k = 3
nb_noires = 5
nb_blanches = 4
nb_rouges = 3

probabilite = proba_tirage_uniforme(k,nb_noires,nb_blanches,nb_rouges)
print(f"La probabilité est : {probabilite:.4f}")
