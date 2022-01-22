def carte_to_chaine(dico):
    """
    Transforme une carte sous forme de dictionnaire et la transforme en 5♦

    @param dico : Une carte
    @type dico : dict

    @return : carte au format d'affichage 4♥
    @rtype : str
    """

    dico_symboles = {"C": chr(9825), "K": chr(9826), "P": chr(9824), "T": chr(9827)}

    assert dico["valeur"] in ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"], "Valeur inconnue"
    assert dico["couleur"] in ["C", "K", "P", "T"], "Couleur inconnue"
    chaine = (" " * (len(dico) - 1)) + dico["valeur"] + dico_symboles[dico["couleur"]]

    return chaine


def affichage_jeu(liste_de_cartes):
    """

    @param liste_de_cartes : Une liste de carte
    @type liste_de_cartes : list
    """
    liste = []
    for carte in liste_de_cartes:
        liste.append(carte_to_chaine(carte))
    if len(liste) == 0:
        print('\n', sep="")
    else:
        print(" ".join(liste) + "\n")
