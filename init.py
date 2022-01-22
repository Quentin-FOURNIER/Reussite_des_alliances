import random
import sys


def init_pioche_fichier(nom_du_fichier="text/data_init_52.txt"):
    """
    Prend un fichier texte des cartes, pour les retourner sous forme de liste.

    @param nom_du_fichier : text/date_init.txt
    @type nom_du_fichier : str

    @return : liste_de_carte_formate : Une liste de carte formatée
    @rtype : list
    """

    # Ouverture fichier :
    try:

        fichier = open(nom_du_fichier, 'r', encoding="utf-8")
        texte = fichier.read()

        # Liste des cartes
        liste_de_cartes = texte.split()
        # Liste de carte au format dictionnaire
        liste_de_carte_formate = []

        # Parcours de la liste de carte, puis formatage
        for carte in liste_de_cartes:
            liste_de_carte_formate.append({"valeur": carte[0:len(carte) - 2], "couleur": carte[-1]})

        # Fermeture fichier
        fichier.close()

        # Retour de la liste formatée
        return liste_de_carte_formate
    except FileNotFoundError:
        sys.exit("Le jeu ne peut contenir que 52 ou 32 cartes.")


def init_pioche_alea(nb_cartes):
    """
    Retourne une pioche mélangée

    @param nb_cartes : 32 ou 52
    @type nb_cartes : int

    @return : pioche mélangée
    @rtype : list
    """

    try:
        pioche = init_pioche_fichier("text/data_init_" + str(nb_cartes) + ".txt")
        random.shuffle(pioche)
        return pioche

    except FileNotFoundError:
        sys.exit("Le jeu ne peut contenir que 52 ou 32 cartes."
                 "\tValeur obtenue" + str(nb_cartes))
